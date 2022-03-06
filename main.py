from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class City(BaseModel):
    city_name : str
    city_weather : str

cities_weather = [
    {"Hafer al-batin": "rainy"},
    {"Riyadh": "disty"},
    {"Abha": "clean"},
    {"Jeddah": "rainy"},
    {"Dammam": "clean"}
]

@app.get("/weather/all")
def greeting():
    return cities_weather

@app.get("/weather/{city}")
def specific_city(city:str):
    for index in range(len(cities_weather)):
        for key in cities_weather[index]:
            if city == key:
                return cities_weather[index]
    
    return "Sorry, We can't found it!"

@app.post("/new-city")
def new_city(city : City):
    global cities_weather
    cities_weather.append({city.city_name:city.city_weather})
    return cities_weather

@app.put("/update-weather/{index}")
def update_weather(city:City, index:int):
    global cities_weather
    cities_weather[index] = {city.city_name : city.city_weather}
    return cities_weather

@app.delete("/delete-city/{index}")
def delete_city(index:int):
    global cities_weather
    del cities_weather[index]
    return cities_weather