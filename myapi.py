from fastapi import FastAPI, HTTPException, Path, Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()
students = {
    1:{
        "name":"john",
        "age":17,
        "class":"year 12"
    }
}
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/")
def index():
    return {"name": "ypur name"}

# PAth parameter
@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(..., description="The ID of the student you want to view", gt=0, lt=3)):
    try:
        return students[student_id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")

# Query parameter

@app.get("/get-by-name")
def get_student(name: str):
    for id in students:
        if(students[id]["name"] == name):
            return students[id]
    return {"Data": "Not Found"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results