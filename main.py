from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Citiyess(BaseModel):
    city :str
    weather:int

Citiyes = [{"city":"Riyadh" , "weather":20} ,
           {"city":"Abha" , "weather":12} ,
           {"city":"Jeddadh" , "weather":30} ,
           {"city":"Dammam" , "weather":28} ]

@app.get("/citiyes/all")
def getCitiyes():
    return Citiyes

@app.get("/city/{city}")
def getCitiy(city : str):
    for i in Citiyes:
        if i['city'] == city:
            return i

@app.post("/city")
def postCity(citiy:Citiyess):
    global Citiyes
    Citiyes.append(citiy)
    return Citiyes

@app.put("/city/{city}")
def putCity(citiy:Citiyess ,city:str,):
    for i in Citiyes:
        if i["city"]== city:
            i = citiy
            return i

@app.delete("/city/{index}")
def deleteCity(index:int):
    del Citiyes[index]
    return Citiyes