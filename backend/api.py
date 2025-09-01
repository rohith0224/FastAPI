import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List



class Fruit(BaseModel):
    name:str
class FruitList(BaseModel):
    fruits: List[Fruit]
app = FastAPI()
origins = ["*"]\

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_db={"fruits":[]}
@app.get("/fruits", response_model=FruitList)
def get_fruits():
    return FruitList(fruits=memory_db["fruits"])
@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return fruit

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)
