import requests
from random import shuffle


class TriviaDB:
    def __init__(self):
        self.my_api = "https://opentdb.com/api.php"

    def define_category(self, chosen_category):
        if chosen_category == "Animals":
            number = 27
        elif chosen_category == "Films":
            number = 11
        elif chosen_category == "Music":
            number = 12
        else:
            number = 23
        return number

    def get_questions(self, amount, category, quiz_type):
        my_params = {
            "amount": amount,
            "category": self.define_category(chosen_category=category),
            "difficulty": "easy",
            "type": quiz_type.lower()
        }
        respond = requests.get(url=self.my_api, params=my_params)
        data = respond.json()["results"]
        final_result = []
        for item in data:
            answers = item["incorrect_answers"]
            answers.append(item["correct_answer"])
            shuffle(answers)
            variable = {
                "category": item["category"],
                "question": item["question"],
                "correct": item["correct_answer"],
                "wrong": answers
            }
            final_result.append(variable)
        return final_result
