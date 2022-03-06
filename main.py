from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


cities = [
     {'city': "Riyadh",
    "weather": "Sunny",
    "degree": 26
  },  {
    'city': "Abha",
    "weather": "Sunny",
    "degree": 22
  },  {
    'city': "Jeddah",
    "weather": "Sunny",
    "degree": 31
  }, {
    'city': "Dammam",
    "weather": "sunny",
    "degree": 27
  },
    {
    'city': "Buraidah",
    "weather": "Rainy",
    "degree": 18
    }
]


class CitiesClass(BaseModel):
    city: str
    weather: str
    degree: int


@app.get("/weather")
def all_weather():
    return cities


@app.get("/weather/{city_x}")
def one_city(city_x: str):
    for x in range(0, len(cities)):
        if city_x in cities[x].values():
            return cities[x]
    else:
        return "This city is not covered in our system! " \
               " or the index of city isn't correct.."


@app.post("/weather/add")
def add_city(new_city: CitiesClass):
    global cities
    cities.append(new_city)
    return cities

@app.put("/weather/change/{index}")
def change_of_weather(weather: CitiesClass, index: int):
    global cities
    cities[index] = weather
    return cities


@app.delete("/weather/delete/{index}")
def del_weather(index: int):
    global cities
    del cities[index]
    return cities


