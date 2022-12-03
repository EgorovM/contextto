from django.urls import path, include
from .views import index, guess, clear_history, get_history, make_guess

from .views import SessionView, GuessView
from .routers import SimpleRouter

router = SimpleRouter()

router.register('session', SessionView)

urlpatterns = [
    path('', index),
    path('guess/', guess),
    path('clear_history/', clear_history),
    path('get_history/', get_history),
    path('make_guess/', make_guess),
    path('api/', include(router.urls)),
    path('api/session/<str:id>/guess', GuessView.as_view({'get': 'list', 'post': 'create'}))
]

