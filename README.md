# Proyecto Individual 1- Data 03- Soy Henry

## Creación de una API

![image](https://user-images.githubusercontent.com/108296379/182138583-9011699a-f009-4454-885e-80dca182b6c8.png)

## Introducción
La API brinda la información solicitada para el proyecto en formato json, para ser ingestada en cualquier otro aplicativo que así lo requiera. 

Los datos se cargan a partir de los ficheros provistos y al no existir necesidad de persistir ningún dato, se trabajaron las consultas y las respuestas enteramente desde python.

Por supesto no se descarga la posibilidad de incluir en el futuro una conección a una base de datos, a modo de persistir los datos.

## Funcionamiento
Para ello se debe descargar el repositorio e instalar los requirements que se encuentran listados. Luego poner en funcionamiento uvicorn con el comando

```bash
uvicorn main:app
```

De esta forma ya se podrá realizar las consultas de forma local.

## Respuestas

Las respuestas de las consultas al **API** devuelven **JSON** y tienen la siguiente estructura:

```json
[
	{
	"Descripción dato 1": valor
	"Descripción dato 2": valor
	...
	}
]
```

## Consultas Disponibles

`/años`: Listado de todos los años de los que se tiene registro, con la cantidad de carreras por año.

`/años/top{numero}`: Listado ordenado con mayor cantidad de carreras por año, en un top según el número indicado.

`/primerpuesto`: Pilotos y la cantidad de veces que consiguieron un primer puesto. Ordenado por cantidad de forma descendente.

`/primerpuesto/top{numero}`: Top de pilotos y la cantidad de veces que consiguieron un primer puesto.

`/circuitos`: Nombre de circuitos con cantidad de carreras que se corrieron en él. Ordenado de más carreras a menos.

`/circuitos/top{numero}`: Top según la cantidad indicada de los nombres de circuitos y carreras.

`/puntos`: Pilotos con carrocería de origen Americano o Británico y la cantidad de puntos acumulados. Ordenados por puntos de forma descendente.

`/puntos/top{numero}`: Top según el numero indicado de pilotos y puntos acumulados con carrocería Americana o Británica.


