import datetime
import uuid
from django.shortcuts import render, redirect

from words.guess import WordGuesser
from words.models import UserSession, DayKeyword, UserGuess, EmailForNotification


def index(request):
    session_id = request.session.get('session_id', uuid.uuid4().hex)
    request.session['session_id'] = session_id

    day_keyword = DayKeyword.objects.last()
    guesser = WordGuesser()

    user_session, created = UserSession.objects.get_or_create(session_id=session_id, keyword=day_keyword)
    guess_history = user_session.userguess_set.order_by("order").all()

    if guess_history.exists():
        last_keyword = guess_history.order_by("datetime").last()
        last_index = last_keyword.id

    # fixme: temporal
    max_word = 2000

    already_saved_email = EmailForNotification.objects.filter(session_id=session_id).exists()

    return render(request, "index.html", locals())


def guess(request):
    if "word" not in request.POST:
        return redirect('/?message=Что-то пошло не так, попробуйте еще раз')

    day_keyword = DayKeyword.objects.last()

    session_id = request.session.get('session_id', uuid.uuid4().hex)
    request.session['session_id'] = session_id
    user_session, created = UserSession.objects.get_or_create(session_id=session_id, keyword=day_keyword)

    guesser = WordGuesser()
    guessed_word = request.POST["word"].strip().lower()

    if not guesser.has_word(guessed_word):
        return redirect(f'/?message=Я не знаю слово "{guessed_word}"')

    order = guesser.guess(guessed_word)

    user_guess, created = UserGuess.objects.get_or_create(session=user_session, word=guessed_word, order=order)

    if not created:
        user_guess.datetime = datetime.datetime.now()
        user_guess.save()

    return redirect('/')


def clear_history(request):
    session_id = uuid.uuid4().hex
    request.session['session_id'] = session_id

    return redirect('/')


def subscript(request):
    session_id = request.session.get('session_id', uuid.uuid4().hex)
    request.session['session_id'] = session_id

    email = request.POST["email"]

    EmailForNotification.objects.create(session_id=session_id, email=email)

    return redirect(f'/?message=Почта "{email}" успешно сохранена!')
