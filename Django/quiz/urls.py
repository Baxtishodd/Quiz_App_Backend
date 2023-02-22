from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("multiple-choice/<str:category>/<str:quantity>", views.first_quiz, name="first-quiz"),
    path("true-false/<str:category>/<str:quantity>", views.second_quiz, name="second-quiz")
]
