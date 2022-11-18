from django.urls import path
from words.views import index, guess

urlpatterns = [
    path('', index),
    path('guess/', guess),
]
