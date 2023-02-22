from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import MyForm
from .trivia_class import TriviaDB
# Create your views here.


def home_page(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["quiz_type"] == "Multiple Choice":
                return HttpResponseRedirect(reverse("first-quiz", kwargs={
                    "quantity": form.cleaned_data["quantity"],
                    "category": form.cleaned_data["category"]
                }))
            else:
                return HttpResponseRedirect(reverse("second-quiz", kwargs={
                    "quantity": form.cleaned_data["quantity"],
                    "category": form.cleaned_data["category"]
                }))

    form = MyForm()
    return render(request, "quiz/index.html", {
        "form": form
    })


def first_quiz(request, category, quantity):
    tool = TriviaDB()
    data = tool.get_questions(
        amount=quantity,
        category=category,
        quiz_type="multiple"
    )
    category_name = data[0]["category"]
    return render(request, "quiz/quiz_first.html", {
        "name": category_name,
        "data": data
    })


def second_quiz(request, category, quantity):
    tool = TriviaDB()
    data = tool.get_questions(
        amount=quantity,
        category=category,
        quiz_type="boolean"
    )
    category_name = data[0]["category"]
    return render(request, "quiz/quiz_second.html", {
        "name": category_name,
        "data": data
    })
