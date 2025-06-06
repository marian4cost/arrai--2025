from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("candidate01", views.candidate01, name="candidate01")
]