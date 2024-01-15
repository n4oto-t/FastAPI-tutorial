from fastapi import FastAPI


app = FastAPI()
fake_item_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# pathパラメーターでない、引数を設定した場合、それはqueryパラメーターとして認識される
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_item_db[skip : skip + limit]


# Optional Parameters
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        # itemを置き換えるのではなく、key-valueのセットを追加する
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# 入力必須のquery parameterを作成するには、デフォルト値を設定しなければ良い
@app.get("items2/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
