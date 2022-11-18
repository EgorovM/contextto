from django.db import models


class DayKeyword(models.Model):
    word = models.CharField(max_length=120)
    date = models.DateField(auto_now=True)


class UserSession(models.Model):
    session_id = models.CharField(max_length=30, unique=True, db_index=True)


class UserGuess(models.Model):
    session = models.ForeignKey(UserSession, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    order = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)