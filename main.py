from fastapi import FastAPI

app = FastAPI()


cities=[{'name':'Riyadh','weather':25},{'name':'Abha','weather':14},{'name':'Jeddah','weather':33},{'name':'Dammam','weather':28}]

@app.get('/')
def Get_All_Cities():
    return {"cities":cities}

@app.get('/city/{name}')
def Get_A_City(name:str):
    for val in range(len(cities)):
        if(name in cities[val]['name']):
            return {cities[val]['name']:cities[val]['weather']}
    return {"":""}

@app.post('/city')
def Add_City(name:str,weather:int):
    global cities
    cities.append({'name':name,'weather':weather})
    return cities[len(cities)-1]

@app.put('/city/{city_name}')
def Update_City(city_name:str,weather:int):
    global cities
    def check(letter):
        if(letter['name']==city_name):
            letter['weather']=weather
        return letter
    list(filter(check,cities))
    return {"cities":cities}

@app.delete('/city/{city_name}')
def Delete_City(city_name:str):
    global cities
    cities=list(filter(lambda city: city['name']!=city_name,cities))
    return {"deleted":city_name,"remained":cities}

    