from fastapi import FastAPI, Query


app = FastAPI()


@app.get("/info")
def read_info(info: str = Query(None, description="정보를 입력해 주세요.")):
    return {"info": info}


@app.get("/items")
def read_items(
    string_query: str = Query(
        default="default value",
        min_length=2,
        max_length=5,
        regex="^[a-zA-Z]+$",
        title="String Query",
        example="abc",
    ),
    number_query: float = Query(
        default=1.0,
        ge=0.5,
        le=10.5,
        title="Number Query",
        example=5.5
    )
):
    return {
        "string_query_handled": string_query,
        "number_query_handled": number_query
    }