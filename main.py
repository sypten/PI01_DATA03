from fastapi import FastAPI
from ETL import años_y_carreras, nombre_carreras, top_nombre_carreras

app= FastAPI(title='Consultas de Corredores',
            description='La API debuelve cuatro tipo de resultados',
            version='0.0.1')

@app.get("/")
async def años():
    return años_y_carreras()

@app.get("/carreras/top{numero}")
async def nombre_top(numero):
    return top_nombre_carreras(numero)

@app.get("/carreras")
async def nombre():
    return nombre_carreras()