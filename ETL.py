import json
import pandas as pd
import numpy as np

with open("./Datasets/constructors.json") as archivo:
    salida = [json.loads(linea) for linea in archivo]
    d_constructors = pd.DataFrame(salida)

with open("./Datasets/drivers.json") as archivo:
    salida = [json.loads(linea) for linea in archivo]
    d_drivers = pd.json_normalize(salida, sep="_")

with open("./Datasets/results.json") as archivo:
    salida = [json.loads(linea) for linea in archivo]
    d_results = pd.DataFrame(salida)

#datos = pd.read_json(ruta_archivo_json, lines=True)
d_pit_stops=pd.read_json("./Datasets/pit_stops.json")
d_circuits=pd.read_csv("./Datasets/circuits.csv")
d_races=pd.read_csv("./Datasets/races.csv")

def años_y_carreras(cantidad : int = 1):
    return [{k:v} for k,v in d_races["year"].value_counts().sort_values(ascending=False).to_dict().items()][:cantidad]

def nombre_carreras():
    carreras=d_races.merge(d_circuits, how= "inner", on="circuitId")
    cant_carreras=carreras["name_y"].value_counts().sort_values(ascending=False)    
    return [{"Nombre circuito":k,"Cantidad de carreras":v} for k,v in cant_carreras.to_dict().items()]

def top_nombre_carreras(numero:int=3):
    numero=int(numero)
    return nombre_carreras()[:numero]