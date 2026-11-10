from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory = "templates")

@app.get("/")
def read_home():
    return {
        "data" : "hello world"
    }

@app.get("/tomato")
def read_tomato(request,Request):
    return templates.TemplateResponse(request, "index.html", {"username": "관리자"})