from django import forms

CATEGORY = [("Animals", "Animals"), ("Films", "Films"), ("Music", "Music"), ("History", "History")]
QUANTITY = [("10", "10"), ("5", "5"), ("15", "15")]
QUIZ_TYPE = [("True / False", "True / False"), ("Multiple Choice", "Multiple Choice")]


class MyForm(forms.Form):
    category = forms.CharField(label='Choose Questions Category:', widget=forms.Select(choices=CATEGORY))
    quiz_type = forms.CharField(label='Define Quiz Type:', widget=forms.Select(choices=QUIZ_TYPE))
    quantity = forms.CharField(label='Define Questions Quantity:', widget=forms.Select(choices=QUANTITY))
