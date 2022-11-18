import uuid
from django.shortcuts import render, redirect

from words.guess import WordGuesser
from words.models import UserSession, DayKeyword, UserGuess


def index(request):
    session_id = request.session.get('session_id', uuid.uuid4().hex)
    request.session['session_id'] = session_id

    day_keyword = DayKeyword.objects.last()
    guesser = WordGuesser(day_keyword.word)

    user_session, _ = UserSession.objects.get_or_create(session_id=session_id)
    guess_history = user_session.userguess_set.order_by("order").all()

    if guess_history.exists():
        last_index = guess_history.order_by("datetime").last().id

    # fixme: temporal
    max_word = guesser.word_count

    return render(request, "index.html", locals())


def guess(request):
    session_id = request.session.get('session_id', uuid.uuid4().hex)
    request.session['session_id'] = session_id
    user_session = UserSession.objects.get(session_id=session_id)

    day_keyword = DayKeyword.objects.last()
    guesser = WordGuesser(day_keyword.word)
    guessed_word = request.POST["word"]

    if not guesser.has_word(guessed_word):
        return redirect(f'/?invalid={guessed_word}')

    order = guesser.guess(request.POST["word"])

    UserGuess.objects.get_or_create(session=user_session, word=guessed_word, order=order)

    return redirect('/')
