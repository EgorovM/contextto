import datetime
import json
import uuid
import pymorphy2

from django.shortcuts import render, redirect
from django.http import JsonResponse

from words.guess import WordGuesser
from words.models import UserSession, DayKeyword, UserGuess


morph = pymorphy2.MorphAnalyzer()


def get_today_keyword() -> DayKeyword:
    today = datetime.datetime.now().date()
    return DayKeyword.objects.filter(date=today).last()


def index(request):
    session_id = request.session.get('session_id', uuid.uuid4().hex)
    request.session['session_id'] = session_id

    day_keyword = get_today_keyword()
    guesser = WordGuesser()

    user_session, created = UserSession.objects.get_or_create(session_id=session_id, keyword=day_keyword)
    guess_history = user_session.userguess_set.order_by("order").all()

    if guess_history.exists():
        last_keyword = guess_history.order_by("datetime").last()
        last_index = last_keyword.id

    # fixme: temporal
    max_word = 2000

    return render(request, "index.html", locals())


def guess(request):
    if "word" not in request.POST:
        return redirect('/?message=Что-то пошло не так, попробуйте еще раз')

    day_keyword = get_today_keyword()

    session_id = request.session.get('session_id', uuid.uuid4().hex)
    request.session['session_id'] = session_id
    user_session, created = UserSession.objects.get_or_create(session_id=session_id, keyword=day_keyword)

    guesser = WordGuesser()
    guessed_word = request.POST["word"].strip().lower().replace("ё", "е")

    if not guesser.has_word(guessed_word):
        return redirect(f'/?message=Я не знаю слово "{guessed_word}"')

    order = guesser.guess(guessed_word)

    user_guess = UserGuess.objects.create(session=user_session, word=guessed_word, order=order)

    if not created:
        user_guess.datetime = datetime.datetime.now()
        user_guess.save()

    return redirect('/')


def clear_history(request):
    session_id = uuid.uuid4().hex
    request.session['session_id'] = session_id

    return redirect('/')


def get_history(request):
    session_id = request.GET['session_id']
    day_keyword = get_today_keyword()
    user_session, _ = UserSession.objects.get_or_create(session_id=session_id, keyword=day_keyword)
    user_guess = []
    orders = set()

    for guess in UserGuess.objects.filter(session=user_session).order_by("-datetime").all():
        if guess.order in orders:
            continue

        user_guess.append(guess)
        orders.add(guess.order)

    return JsonResponse({
        "guess_history": sorted([ug.serialize() for ug in user_guess], key=lambda x: x["order"])
    })


def get_attempts(request):
    session_id = request.GET['session_id']
    day_keyword = get_today_keyword()
    user_session, _ = UserSession.objects.get_or_create(session_id=session_id, keyword=day_keyword)
    user_guess = UserGuess.objects.filter(session=user_session).order_by("datetime")

    return JsonResponse({
        "guess_history": [ug.serialize() for ug in user_guess]
    })


def make_guess(request):
    session_id = request.GET['session_id']
    day_keyword = get_today_keyword()
    user_session, _ = UserSession.objects.get_or_create(session_id=session_id, keyword=day_keyword)

    guesser = WordGuesser()
    guessed_word = json.loads(request.body.decode("utf-8"))["word"].strip().lower().replace("ё", "е")

    if not guesser.has_word(guessed_word):
        return JsonResponse({"error_text": f"Я не знаю слово {guessed_word}"}, status=400)

    order = guesser.guess(guessed_word)

    user_guess = UserGuess.objects.create(session=user_session, word=guessed_word, order=order)

    return JsonResponse({
        "guess_history": [user_guess.serialize()]
    })
