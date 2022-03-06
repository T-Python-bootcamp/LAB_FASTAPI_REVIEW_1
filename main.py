
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

cities_weather = [{"city":"Riyadh","weather":22.3 },{"city":"Abha","weather":55 } , {"city":"Jeddadh","weather":34 }, {"city":"Dammam","weather":21 }]

class Cities(BaseModel):
    city:str
    weather:float


@app.get("/city")
def get_all_cities():
    return cities_weather

@app.get("/city/{city}")
def get_a_city(city:str ):
    for c in cities_weather:
        if c["city"]==city:
            return c
        else:
            return ({"msg":f"the city {city} is not exist"})

@app.post("/city")
def create_city(newCity:Cities):
    global cities_weather
    cities_weather.append(newCity)
    return cities_weather

@app.put("/city/{city}")
def update_city(city:str,newCity:Cities):
    for c in cities_weather:
        if c["city"]==city:
            c=newCity
            return c
        else:
            return ({"msg":f"the city {city} is not exist"})

@app.delete("/city/{index}")
def delete_city(index:int):
    del cities_weather[index]
    return cities_weather
