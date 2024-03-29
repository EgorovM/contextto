from django.db import models


class DayKeyword(models.Model):
    word = models.CharField(max_length=120)
    date = models.DateField(null=True)


class UserSession(models.Model):
    session_id = models.CharField(max_length=30, db_index=True)
    keyword = models.ForeignKey(DayKeyword, on_delete=models.CASCADE)


class UserGuess(models.Model):
    session = models.ForeignKey(UserSession, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    order = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)

    def serialize(self):
        return {"id": self.id, "word": self.word, "order": self.order, "timestamp": self.datetime.timestamp()}


class Word(models.Model):
    word = models.CharField(max_length=128)
