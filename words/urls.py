from django.urls import path
from words.views import index, guess, clear_history, get_history, make_guess, get_attempts

urlpatterns = [
    path('', index),
    path('guess/', guess),
    path('clear_history/', clear_history),
    path('get_history/', get_history),
    path('make_guess/', make_guess),
    path('get_attempts/', get_attempts),
]
