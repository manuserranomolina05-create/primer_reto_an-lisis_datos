#Consulta, tratamiento y análisis de datos meteorológicos : 
1#Exploramos la api:
{
  "latitude": 37.785587,
  "longitude": -3.7349243,
  "generationtime_ms": 267.25161075592,
  "utc_offset_seconds": 3600,
  "timezone": "Europe/Madrid",
  "timezone_abbreviation": "GMT+1",
  "elevation": 486,
  "daily_units": {
    "time": "iso8601",
    "temperature_2m_mean": "°C",
    "temperature_2m_max": "°C",
    "temperature_2m_min": "°C"
  },
  "daily": {
    "time": [
      "2025-01-01",
      "2025-01-02",
      "2025-01-03",
      "2025-01-04",
      "2025-01-05",
      "2025-01-06",
      "2025-01-07",
      "2025-01-08",
      "2025-01-09",
      "2025-01-10",
      "2025-01-11",
      "2025-01-12",
      "2025-01-13",
      "2025-01-14",
      "2025-01-15",
      "2025-01-16",
      "2025-01-17",
      "2025-01-18",
      "2025-01-19",
      "2025-01-20",
      "2025-01-21",
      "2025-01-22",
      "2025-01-23",
      "2025-01-24",
      "2025-01-25",
      "2025-01-26",
      "2025-01-27",
      "2025-01-28",
      "2025-01-29",
      "2025-01-30",
      "2025-01-31"
    ],
      
    "temperature_2m_mean": [7.1, 7.3, 7.4, 8.1, 9.5, 10.2, 7.1, 8.3, 12.3, 10.3, 12, 10.6, 6, 4.3, 5.2, 5.2, 5.1, 6, 6.3, 7.5, 12.8, 14.4, 12.6, 10.4, 10.2, 11.3, 14.8, 9.1, 8.1, 7.4, 6.6],
    "temperature_2m_max": [12.8, 12.9, 12.9, 12.6, 15.8, 12, 10.8, 15.2, 15.7, 14.6, 14.8, 14.1, 11, 10.7, 10.9, 9.1, 11.2, 11.1, 11.4, 13, 17.5, 18.6, 17.1, 16, 13.5, 17.5, 16.8, 11.1, 11.9, 10.5, 10.5],
    "temperature_2m_min": [2.4, 2.5, 3, 3.9, 3.5, 7.4, 3.1, 3.7, 9.2, 7, 9.5, 7.1, 0.9, -1.1, 0, 2.5, 0, 2.2, 1.9, 2.4, 9.1, 10.2, 9.4, 5.8, 6.1, 4.1, 10.3, 6.8, 3.2, 5.2, 3.5]
  }
}

# 1.1 ¿Qué información proporciona el servicio?
# El servicio proporciona datos meteorológicos de una ciudad, organizados dentro de un diccionario.

# 1.2 ¿Qué significan latitude y longitude?
# Latitude indica la latitud en la que se encuentra la ciudad de Jaén y longitude indica su longitud.

# 1.3 ¿Qué fechas se están consultando?
# Se consultan los datos correspondientes a todo el mes de enero.

# 1.4 ¿Qué información solicita temperature_2m_mean?
# Solicita la temperatura media registrada a dos metros de altura.

# 1.5 ¿Qué información proporcionan temperature_2m_max y temperature_2m_min?
# Indican las temperaturas máximas y mínimas registradas a dos metros de altura.

# 1.6 ¿Qué diferencias observas entre esa respuesta y una lista de Python?
# La respuesta está organizada en un diccionario mediante claves y valores, mientras que una lista almacena los datos de forma ordenada mediante posiciones.

# 1.7 ¿Qué ocurriría si cambiásemos end_date para consultar hasta el 15 de enero?
# La API devolvería solamente los datos desde el 1 hasta el 15 de enero, por lo que las listas tendrían 15 elementos en lugar de 31.

# 1.8 ¿Qué ventaja tiene consultar una API frente a introducir los datos manualmente?
# La API permite obtener los datos automáticamente y ahorra tiempo, ya que no tenemos que introducirlos uno por uno.


# 2. Realizamos una petición desde Python.

# 2.1 ¿Para qué sirve import requests?
# Sirve para importar la biblioteca requests, que nos permite realizar peticiones HTTP y obtener datos de una API.

# 2.2 ¿Qué tipo de objeto es parametros?
# Es un diccionario de Python que almacena información mediante pares de clave y valor.

# 2.3 ¿Qué diferencia hay entre url y parametros?
# La URL es la dirección a la que realizamos la petición, mientras que los parámetros son los valores que enviamos para indicar qué información queremos obtener.

# 2.4 ¿Qué hacen timeout=30 y raise_for_status()?
# timeout=30 establece un tiempo máximo de 30 segundos para recibir respuesta. raise_for_status() comprueba si la petición ha devuelto algún error HTTP.

# 2.5 ¿Qué diferencia hay entre respuesta y datos?
# Respuesta es el objeto que recibimos al realizar la petición HTTP. Datos es la información que extraemos de esa respuesta.

# 2.6 ¿Qué podría ocurrir si falla la conexión o el servidor devuelve un error?
# Si falla la conexión, el programa puede mostrar un error y detenerse si no lo controlamos. También puede ocurrir que el servidor devuelva un código de error.

# 2.7 ¿Por qué separamos los parámetros de la dirección URL?
# Los separamos para que el código esté más organizado y sea más fácil modificar los valores.

# 2.8 ¿En qué se diferencia una petición GET de una petición POST?
# GET se utiliza principalmente para solicitar información a un servidor, mientras que POST se utiliza para enviar datos.


# 3. Exploramos la estructura de los datos.

# 3.1 ¿Qué valores tienen las claves latitude y longitude?
# latitude: 37.785587
# longitude: -3.7349243

# 3.2 ¿Qué claves contiene daily?
# Contiene las siguientes claves: time, temperature_2m_mean, temperature_2m_max y temperature_2m_min.

# 3.3 ¿Qué unidades se utilizan para la temperatura?
# Se utilizan grados Celsius (°C).
generationtime_ms	0.11861324310302734
utc_offset_seconds	3600
timezone	"Europe/Madrid"
timezone_abbreviation	"GMT+1"
elevation	486.0JS:486
daily_units	
time	"iso8601"
temperature_2m_mean	"°C"
temperature_2m_max	"°C"
temperature_2m_min	"°C"

import requests

url = "https://archive-api.open-meteo.com/v1/archive"
parametros = {
    "latitude": 37.7796,
    "longitude": -3.7849,
    "start_date": "2025-01-01",
    "end_date": "2025-01-31",
    "daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min",
    "timezone": "Europe/Madrid",
}

respuesta = requests.get(url, params=parametros, timeout=30)
respuesta.raise_for_status()
datos = respuesta.json()

print(datos)

print(type(url))
print(type(parametros))
print(respuesta.url)
diarios = datos["daily"]
print(diarios.keys())
