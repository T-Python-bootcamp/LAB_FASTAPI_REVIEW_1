from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class City_Weather(BaseModel):
    name: str
    weather:int
    
cities = {"Riyadh":29, "Abha":14, "Jeddah":33, "Dammam":32}

@app.get("/cities")
def get_all():
    return cities

@app.get("/cities/{city}")
def get_one(city:str):
    global cities
    return cities[city]

@app.post("/cities/add")
def add_city(city:str, weather:int):
    global cities
    cities.update({city : weather})
    return cities

@app.put("/cities/update")
def update_city(city:str, weather:int):
    global cities
    update_city = {city:weather}
    cities.update(update_city)
    return cities

@app.delete("/cities/delete")
def delete_city(city:str):
    global cities
    cities.pop(city)
    return cities