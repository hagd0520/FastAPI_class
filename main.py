from fastapi import FastAPI, Query


app = FastAPI()


# @app.get("/users")
# def read_users(q: str = Query(None, max_length=50)):
#     return {"q": q}


@app.get("/items")
def read_items(internal_query: str = Query(None, alias="search")):
    return {"query_handled": internal_query}


@app.get("/users")
def read_users(q: str = Query(None, deprecated=True)):
    # 특정 쿼리 파라미터가 더이상 사용되지 않을 것임을 암시
    return {"q": q}