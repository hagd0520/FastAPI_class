from fastapi import FastAPI
from starlette.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse


app = FastAPI()


@app.get("/json", response_class=JSONResponse)
def read_json():
    # JSON 은 기본값으로서 사용되기 때문에 큰 의미는 없다
    return {"msg": "This is JSON"}


@app.get("/html", response_class=HTMLResponse)
def read_html():
    return "<h1>This is HTML</h1>"


@app.get("/text", response_class=PlainTextResponse)
def read_text():
    return "This is Plain Text"


@app.get("/redirect")
def read_redirect():
    return RedirectResponse(url="/text")