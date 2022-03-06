import re
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Info(BaseModel):
    name1: str
    weather: int
# Start with those 4 citiyes : Riyadh , Abha, Jeddadh, Dammam



dict1={"Rafha":12,"damamm":44,"ryadh":23}


@app.get("/")
def great():
    return dict1


# @app.get("/city/{name}")
# def get_name(name:str):
#     return {"weather":dict1[name]}
    # ترجع بالاسم درحه الحراره
@app.get("/city/{name}")
def get_name(name:str):
    if name in dict1:
        return {"weather":dict1[name]}
    else:
        return "the city not found"

        # هنا نتحقق اذا مو موجوده يطلع له رساله 

@app.post("/add/city")
def createcity(city:Info):
    global dict1
    dict1.update({city.name1 :city.weather})
    return dict1

@app.put("/cities/update")
def update_city(city:Info):
    if city.name1 in dict1:
        dict1[city.name1]==city.weather
        return dict1    
    else:
        return "the city is not exist"

@app.delete("/city/del/{key}")
def del_city(key:str):
    global dict1
    del dict1[key]
    return dict1



# list1 = [{"name": "abha", "weather": 12}, {"name": "Ryiadh", "weather": 45}, {
#     "name": "Jeddadh", "weather": 44}, {"name": "Dammam", "weather": 50}]


# @app.get("/")
# def info():
#     return list1


# @app.get("/info/{name}/{weather}")
# def info_citis(name: str):
#     for x in list1:
#         if x["name"]==name:
#              return x
#         else:
#             return {"Your city does not exist"}


# @app.post("/addsity/info")
# def creatr_city(info_1: Info):
#     global list1
#     list1.append(info_1.name1)
#     list1.append(info_1.weather)

#     return list1


# @app.put("/city/update/{index}")
# def update_citys(informaiton: Info, index: int):
#     global list1
#     list1[index]=informaiton.weather
#     list1[index] = informaiton.name1 
#     return list1


# @app.delete("/cites/del/{index}")
# def dele_city(index: int):
#     global list1
#     del list1[index]
#     return list1
