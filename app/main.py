from fastapi import FastAPI
import uvicorn
from connexion import DataAccess as da

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bonjour, bienvenue sur l'API restaurants"}

   # - infos d'un restaurant à partir de son id,
@app.get("/api/info/{resto_id}")
async def restaurant_by_id(resto_id=None):
    result = da.get_restaurant_by_id(resto_id)
    return result

   # - liste des noms de restaurants à partir du type de cuisine,
@app.get("/api/cuisine/{resto_type}")
async def restaurant_by_cuisine_type(resto_type=None):
    result = da.get_restaurant_by_cuisine_type(resto_type)
    return result

   # - nombre d'inspection d'un restaurant à partir de son id restaurant,
@app.get("/api/inspections/{resto_id}")
async def nb_inspections_by_id(resto_id=None):
    result = da.get_nb_inspections_by_id(resto_id)
    return result

   # - noms des 10 premiers restaurants d'un grade donné.
@app.get("/api/topgrade/{grade}")
async def get_10_first_by_grade(grade=None):
    result = da.get_10_first_by_grade(grade)
    return result