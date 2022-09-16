from fastapi import FastAPI
from ETL import años_carreras, top_años_carreras, primer_puesto,top_primer_puesto, nombre_circuito, top_nombre_circuito, pilotos_puntos, top_pilotos_puntos

app= FastAPI(title='Consultas de Corredores',
            description='La API devuelve cuatro tipo de resultados principales /años, /circuitos, /primerpuesto /puntos. A todos se les puede agregar /top{numero} para realizar un top de los valores',
            version='1.0.0')

@app.get("/años")
async def años():
    return años_carreras()

@app.get("/años/top{numero}")
async def top_años(numero):
    return top_años_carreras(numero)

@app.get("/primerpuesto")
async def primerpuesto():
    return primer_puesto()

@app.get("/primerpuesto/top{numero}")
async def top_primerpuesto(numero):
    return top_primer_puesto(numero)

@app.get("/circuitos")
async def circuito():
    return nombre_circuito()

@app.get("/circuitos/top{numero}")
async def top_circuito(numero):
    return top_nombre_circuito(numero)

@app.get("/puntos")
async def puntos_ame_bri():
    return pilotos_puntos()

@app.get("/puntos/top{numero}")
async def top_puntos_ame_bri(numero):
    return top_pilotos_puntos(numero)


