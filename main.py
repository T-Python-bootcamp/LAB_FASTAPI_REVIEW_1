from fastapi import FastAPI
from pydantic import BaseModel

class City(BaseModel):
    name : str
    temp : int


app = FastAPI()

cities = {"Riyadh":34 ,
    "Abha" : 14  ,
    "Jeddadh" :  40  ,
    "Dammam":32 }

@app.get("/cities/all")
def get_cities():
    return cities

@app.get("/cities/{city}")
def get_city(city:str):
    if city in cities :
        return "weather" , cities[city]
    else :
        return "The city is not found"


@app.post("/cities/add")
def create_city( city : City):
    global cities
    cities.update({city.name:city.temp})
    return  cities

@app.put("/cities/edit")
def update_city(city : City):
    global cities
    cities.update({city.name: city.temp})
    if city.name is not None:
        return cities
    else :
        return "city is not found"

@app.delete("/cities/delete/{city}")
def delete_city(city : str):
    global cities
    del cities[city]
    return cities

