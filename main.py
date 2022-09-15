from fastapi import FastAPI
from ETL import años_carreras, primer_puesto, top_años_carreras, nombre_circuito, top_nombre_circuito, pilotos_puntos

app= FastAPI(title='Consultas de Corredores',
            description='La API devuelve cuatro tipo de resultados principales /años, /circuitos, /pilotos, /puntos. A todos se les puede agregar /top{numero} para realizar un top de los valores',
            version='0.1.1')

@app.get("/años")
async def años():
    return años_carreras()

@app.get("/años/top{numero}")
async def top_años(numero):
    return top_años_carreras(numero)

@app.get("/circuito")
async def circuito():
    return nombre_circuito()

@app.get("/circuito/top{numero}")
async def circuito_top(numero):
    return top_nombre_circuito(numero)

@app.get("/pilotos")
async def pilotos():
    return pilotos_puntos()

@app.get("/primeros")
async def primeros():
    return primer_puesto()