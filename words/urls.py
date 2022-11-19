from django.urls import path
from words.views import index, guess, clear_history

urlpatterns = [
    path('', index),
    path('guess/', guess),
    path('clear_history/', clear_history),
]
