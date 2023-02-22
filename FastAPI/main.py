from fastapi import FastAPI, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from trivia_class import TriviaDB

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home_get_page(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })


@app.post("/")
def home_post_page(request: Request, category: str = Form(), quantity: str = Form(), quiz_type: str = Form()):
    if quiz_type == "Multiple Choice":
        redirect_url = app.url_path_for("first_quiz_page", chosen_category=category, chosen_quantity=quantity)
    else:
        redirect_url = app.url_path_for("second_quiz_page", chosen_category=category, chosen_quantity=quantity)
    return RedirectResponse(url=f"{redirect_url}", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/multiple-choice/{chosen_category}/{chosen_quantity}")
def first_quiz_page(request: Request, chosen_category: str, chosen_quantity: str):
    tool = TriviaDB()
    data = tool.get_questions(
        amount=chosen_quantity,
        category=chosen_category,
        quiz_type="multiple",
    )
    category_name = data[0]["category"]
    return templates.TemplateResponse("quiz_first.html", {
        "request": request,
        "data": data,
        "name": category_name
    })


@app.get("/true-false/{chosen_category}/{chosen_quantity}")
def second_quiz_page(request: Request, chosen_category: str, chosen_quantity: str):
    tool = TriviaDB()
    data = tool.get_questions(
        amount=chosen_quantity,
        category=chosen_category,
        quiz_type="boolean",
    )
    category_name = data[0]["category"]
    return templates.TemplateResponse("quiz_second.html", {
        "request": request,
        "data": data,
        "name": category_name
    })