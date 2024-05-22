from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/items")
def read_items(request: Request):
    my_items = ["apple", "banana", "cherry"]
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "items": my_items}
    )
    
    
@app.get("/dynamic_items")
def dynamic_items(request: Request, item_list: str = ""):
    items = item_list.split(",")
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "items": items}
    )
    
    
@app.get("/inherit")
def template_inherit(request: Request):
    my_text = "FastAPI와 Jinja2를 이용한 예시입니다."
    return templates.TemplateResponse(
        "inherit.html",
        {"request": request, "text": my_text}
    )
    