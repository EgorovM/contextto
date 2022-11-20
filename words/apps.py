from django.apps import AppConfig


class WordsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'words'

    def ready(self):
        from words.models import DayKeyword, Word
        from words.guess import WordGuesser

        day_keyword = DayKeyword.objects.last()

        # fixme: temporal
        if not day_keyword:
            day_keyword = DayKeyword.objects.create(word="вода")

        print("initializing app")
        WordGuesser(day_keyword.word, [word.word for word in Word.objects.all()])
        print("app started!")
