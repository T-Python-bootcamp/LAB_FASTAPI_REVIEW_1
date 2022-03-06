import re
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Info(BaseModel):
    name1: str
    weather: int
# Start with those 4 citiyes : Riyadh , Abha, Jeddadh, Dammam


list1 = [{"name": "abha", "weather": 12}, {"name": "Ryiadh", "weather": 45}, {
    "name": "Jeddadh", "weather": 44}, {"name": "Dammam", "weather": 50}]


@app.get("/")
def info():
    return list1


@app.get("/info/{name}/{weather}")
def info_citis(name: str, weather: int):
    return {"msg": f"hello you are from {name} and weather your CityP{weather}"}


@app.post("/addsity/info")
def creatr_city(info_1: Info):
    global list1
    list1.append(info_1.name1)
    list1.append(info_1.weather)

    return list1


@app.put("/city/update/{index}")
def update_citys(informaiton: Info, index: int):
    global list1
    list1[index] = informaiton.name1
    return list1


@app.delete("/cites/del/{index}")
def dele_city(index: int):
    global list1
    del list1[index]
    return list1
