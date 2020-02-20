from django.urls import path
from . import views

app_name = 'yahtzee_app'

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('login/process', views.login_process),
    path('register', views.register),
    path('register/process', views.register_process),
    path('lobby', views.lobby),
    path('lobby_process', views.lobby_process),
    path('game', views.game),
    path('game_process/<int:num>', views.game_process),
    path('probability', views.probability, name="probability"),
    path('probability/plot', views.img_plot, name="img_plot"),
    path('log_out', views.log_out),

    path('benis',views.benis)
]
