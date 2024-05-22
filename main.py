from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates", auto_reload=True)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "username": "John Doe"})