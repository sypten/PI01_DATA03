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

def años_carreras():
    return [{"Año":k,"carreras":v} for k,v in d_races["year"].value_counts().sort_values(ascending=False).to_dict().items()]

def top_años_carreras(numero : int = 3):
    numero=int(numero)
    return años_carreras()[:numero]

def nombre_circuito():
    carreras=d_races.merge(d_circuits, how= "inner", on="circuitId")
    cant_carreras=carreras["name_y"].value_counts().sort_values(ascending=False)    
    return [{"Nombre circuito":k,"Cantidad de carreras":v} for k,v in cant_carreras.to_dict().items()]

def top_nombre_circuito(numero:int=3):
    numero=int(numero)
    return nombre_circuito()[:numero]

def pilotos_puntos():
    bri_ame=d_constructors[(d_constructors.nationality=="British") | (d_constructors.nationality=="American")]
    res_bri_ame=d_results.merge(bri_ame,how='inner',on="constructorId")
    resname_bri_ame=res_bri_ame.merge(d_drivers,how="left",on="driverId")
    resname_bri_ame["nombre"]=resname_bri_ame["name_forename"]+" "+resname_bri_ame["name_surname"]
    resultado=resname_bri_ame[["driverId","nombre","points"]].groupby(["driverId","nombre"]).sum("points").sort_values("points",ascending=False)
    resultado.reset_index(inplace=True)
    return resultado.to_dict(orient="records")