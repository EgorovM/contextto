from django.contrib import admin
from words import models


admin.site.register(models.UserSession)
admin.site.register(models.UserGuess)
admin.site.register(models.DayKeyword)
admin.site.register(models.Word)
