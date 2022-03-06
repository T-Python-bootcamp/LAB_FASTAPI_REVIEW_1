from typing import Optional
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel

app = FastAPI()

cities = {"Riyadh": 45 , "Abha": 24, "Jeddadh": 37, "Dammam": 43}

class City(BaseModel):
    name: str
    weather: int

@app.get("/")
async def get_cities(city: Optional[str] = None):
    if city:
        if city in cities:
            return cities[city]
        else:
            raise HTTPException(status_code= 404, detail = "Inof about entered city is not found")
    else:
        return cities
        
@app.post("/city")
async def add_city(city: City):
    cities[city.name] = city.weather

    return cities

@app.put("/city")
async def update_city(city: City):
    if city.name in cities:
        cities[city.name] = city.weather
        return cities
    else:
        raise HTTPException(status_code = 400, detail = "Provided city is not exist")

@app.delete("/city")
async def delete_city(city:str = Body(...)):
    if city in cities:
        del cities[city]
        return cities
    else:
        raise HTTPException(status_code = 400, detail = "Provided city is not exist")