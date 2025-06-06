from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vote_king", views.vote_king, name="vote_king"),
    path("vote_queen", views.vote_queen, name="vote_queen"),
]