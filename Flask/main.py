from flask import Flask, render_template, request, redirect, url_for
from forms import MyForm
from trivia_class import TriviaDB

app = Flask(__name__)
app.config["SECRET_KEY"] = "TommyShelby"


@app.route("/", methods=["GET", "POST"])
def home_page():
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if form.quiz_type.data == "Multiple Choice":
                return redirect(url_for("first_quiz_page",
                                        quantity=form.quantity.data,
                                        category=form.category.data
                                        )
                                )
            else:
                return redirect(url_for("second_quiz_page",
                                        quantity=form.quantity.data,
                                        category=form.category.data
                                        )
                                )
    return render_template("index.html", form=form)


@app.route("/quiz/multiple-choice")
def first_quiz_page():
    tool = TriviaDB()
    data = tool.get_questions(
        amount=request.args.get("quantity"),
        category=request.args.get("category"),
        quiz_type="multiple"
    )
    category_name = data[0]["category"]
    return render_template("quiz_first.html", data=data, name=category_name)


@app.route("/quiz/true-false")
def second_quiz_page():
    tool = TriviaDB()
    my_data = tool.get_questions(
        amount=request.args.get("quantity"),
        category=request.args.get("category"),
        quiz_type="boolean"
    )
    category_name = my_data[0]["category"]
    return render_template("quiz_second.html", data=my_data, name=category_name)


if __name__ == "__main__":
    app.run(debug=True)
