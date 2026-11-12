import statistics
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
#3.4. ¿Qué tipos de dato devuelven diarios y responde: type(datos['daily']) , type(datos['daily']['time']) y type(datos['daily']["temperature_2m_mean"]) ?
#En los datos daily son datos de tipo nombre, de time son datos integer, temperature 2m_mean tienen datos de temperatura.
#3.5. ¿Cuántas fechas y temperaturas has obtenido?
  #"start_date": "2025-01-01",
   # "end_date": "2025-01-31",
#Las que escoge las fechas de inicio y las fechas de final .
#Temperaturas son la temperatura media, la temperauta máxima y la temperatura mínima.
#3.6 Comprueba que las listas de fechas, temperaturas medias, máximas y mínimas tienen la misma longitud. ¿Por qué deben coincidir?
#Deben de conocer los datos en el núemro.
#3.7. Muestra la primera fecha, la temperatura media del primer día y la máxima del último.
#"temperature_2m_mean": [7.1, 7.3, 7.4, 8.1, 9.5, 10.2, 7.1, 8.3, 12.3, 10.3, 12, 10.6, 6, 4.3, 5.2, 5.2, 5.1, 6, 6.3, 7.5, 12.8, 14.4, 12.6, 10.4, 10.2, 11.3, 14.8, 9.1, 8.1, 7.4, 6.6],
 #   "temperature_2m_max": [12.8, 12.9, 12.9, 12.6, 15.8, 12, 10.8, 15.2, 15.7, 14.6, 14.8, 14.1, 11, 10.7, 10.9, 9.1, 11.2, 11.1, 11.4, 13, 17.5, 18.6, 17.1, 16, 13.5, 17.5, 16.8, 11.1, 11.9, 10.5, 10.5],
  #  "temperature_2m_min": [2.4, 2.5, 3, 3.9, 3.5, 7.4, 3.1, 3.7, 9.2, 7, 9.5, 7.1, 0.9, -1.1, 0, 2.5, 0, 2.2, 1.9, 2.4, 9.1, 10.2, 9.4, 5.8, 6.1, 4.1, 10.3, 6.8, 3.2, 5.2, 3.5]
  #}
#}
#7.1 es la temperatura media del primer día y y la máxima del último día sería de 
#3.8 ¿Qué sucede si intentas acceder a una posición que no existe?
#Si accedemos a una posición que no existe, nos daría un valor que sería cero
#3.9) ¿Cómo comprobarías si una clave está presente antes de utilizarla?
#Recorreriamos mediante un bucle for el diccionario .

#4)Calcula estadísticas con las temperaturas:

temperaturas = datos['daily']["temperature_2m_mean"] print(temperaturas)
#4.1. ¿Cuáles son las cinco primeras y las cinco últimas temperaturas?
#4) "temperature_2m_mean": [7.1, 7.3, 7.4, 8.1, 9.5]
#"temperature_2m_max": [12.8, 12.9, 12.9, 12.6, 15.8]
#  "temperature_2m_min": [2.4, 2.5, 3, 3.9, 3.5]
#4.2 ¿Cuántos valores contiene la lista?
#Cada una de las temperaturas tienen 31 valores .
#4.3) ¿Cuál es la diferencia entre la temperatura más alta y la más baja?
#Temperatura máxima: 17,5 °C.
#Temperatura mínima: 4,1 °C.
#4.4) diferencias = [
    #maximo - minimo
    #for maximo, minimo in zip(
        #temperature_2m_max,
        #temperature_2m_min
    #)
#]

#4.5. Crea una lista con las temperaturas superiores a 15 °C y otra con temperaturas inferiores a 10 °C.

temperaturas_superior = [temp for temp  in temperatura if temp > 15 ]
temperatura_bajas = [temp for temp in temperaturas if temp < 10]
#creamos la lista , y dentro ejecutamos un for que nos lo busque en el dicionario de temperaturas y con el if le metemos la condición .

print("Temperaturas superiores a 15 ºC:", temperaturas_altas)
print("Temperaturas inferiores a 10 ºC:", temperaturas_bajas)
#4.6 mediante un print, imprimimos cada una de las temperaturas .

#4.7  Comprueba si todas las temperaturas son superiores a 0 °C y si alguna supera los 20 °C.
#comprobamos si las temperaturas son superiores a cero, y si alguna supera los 20 :
todas_mayores_cero = all(temp > 0 for temp in temperaturas)
alguna_mayor_veinte = any(temp > 20 for temp in temperaturas)
#4.8 Ordena las temperaturas de menor a mayor sin alterar la lista original :
alguna_mayor_veinte = dict(temp  for temp in temperaturas)

#5.1 Transforma y filtra datos :
# f = ((9 / 5)*C + 32)
#convertimos de grados centigrados a fahrenheit :
def grados_fahrenhetit():
    for temp in temperaturas:
        temp = ((9 / 5)*temp + 32)
return(print(f"los grados fahrenheit son {temp}")
#5.2. Crea listas con temperaturas en dos rangos, un rango con las temperaturas menor o igual a la media y otra como superior a la media, usa las temperaturas en ºC.
# 5. Transformar y filtrar datos
fahrenheit = [(t * 9/5) + 32 for t in temperaturas]
print("En Fahrenheit:", fahrenheit)

media_mes = sum(temperaturas) / len(temperaturas)
menor_media = [t for t in temperaturas if t <= media_mes]
mayor_media = [t for t in temperaturas if t > media_mes]

clasificacion_15 = ["inferior" if t < 15 else ("igual" if t == 15 else "superior") for t in temperaturas]

indices_15 = [i for i, t in enumerate(temperaturas) if t > 15]
print("Índices días > 15ºC:", indices_15)

tuplas_cf = [(t, (t * 9/5) + 32) for t in temperaturas]

variacion = [round(temperaturas[i] - temperaturas[i-1], 2) for i in range(1, len(temperaturas))]
print("Variación diaria:", variacion)

dias_tipo = [
    "frío" if t < 7 else ("templado" if t <= 12 else "cálido") 
    for t in temperaturas
]
print("Tipos de día:", dias_tipo)
#clasifica cada temperatura como inferior, igual o superior a 15 
def rangos():
    for temp in temperaturas:
print(max(diferencias))
#6:Relaciona cada valor con su fecha:
#fecha: {
    #"media": media,
    #"maxima": maxima,
    #"minima", minima
    #}
amplitudes_diarias = {}
for fecha, valores in registros_meteorologicos.items():
    amplitud = valores['maxima'] - valores['minima']
    amplitudes_diarias[fecha] = round(amplitud, 2)

print("Amplitud térmica diaria:", amplitudes_diarias)
#7:Analiza el periodo:
#Calcula medidas descriptivas para las temperaturas medias, máximas y mínimas.  Estas son: Media aritmética: es el valor que obtenemos al sumar todas las temperaturas y dividir el resultado entre el número de temperaturas. Mediana: es el valor que queda en el centro cuando ordenamos todas las temperaturas de menor a mayor (si tenemos un número impar de temperaturas, la mediana es el valor central, si tenemos un número par, la mediana es la media de los dos valores centrales) Valor máximo y mínimo: son, respectivamente, el mayor y el menor valor del conjunto. Rango: es la diferencia entre el valor máximo y el valor mínimo.Varianza: es una medida que indica cuánto se alejan, en conjunto, los valores respecto a la media, para calcularla, se determina la diferencia entre cada temperatura y la media, se elevan esas diferencias al cuadrado y se calcula su promedio Desviación típica: es la raíz cuadrada de la varianza. Nos permite medir la dispersión de los valores. Escribe conclusiones explicando qué significa cada resultado. No presentes únicamente números: indica qué muestran sobre el periodo estudiado.

#media = statics.mean(temperaturas) lo hacemos para lograr la temperatura
#1 media aritmetica:
media = []
for temp in temperaturas:
    media = statistics.mean(temperaturas)
    media += 1
print(media)

media = []
for temp in temperaturas:
    mediana = mediana = statistics.median(temperaturas)
    mediana += 1
print(f" la mediana es {mediana}")

#calculamos el maximo = max(temperaturas)
minimo = min(temperaturas)
rango = maximo - minimo
print(rango)
#desviación típica ( o estandar)
varianza = statistics.pvariance(temperaturas)
print(varianza )
#6.Desviacion tipica :
desviacion_tipica = statistics.pstdev(temperaturas)
print(desviacion_tipica )
    
#8 Estudiamos la evolucion temporal :
#8.1. Muestra las temperaturas medias junto con sus fechas:
for temp in temp       
#8.2 Filtra la primera semana y la segunda quincena
import statistics
import matplotlib.pyplot as plt

fechas  = datos["daily"]["time"]
medias  = datos["daily"]["temperature_2m_mean"]
maximas = datos["daily"]["temperature_2m_max"]
minimas = datos["daily"]["temperature_2m_min"]
for fecha, temp in zip(fechas, medias):
    print(fecha, temp)
    primera_semana   = list(zip(fechas[:7], medias[:7]))     # días 1 al 7
segunda_quincena = list(zip(fechas[15:], medias[15:]))   # días 16 al 31

print("Primera semana:", primera_semana)
print("Segunda quincena:", segunda_quincena)
#8.3  Calcula las variaciones entre días consecutivos e identifica el mayor aumento y descenso.
variaciones = [round(medias[i] - medias[i-1], 2) for i in range(1, len(medias))]

mayor_aumento = max(variaciones)
mayor_descenso = min(variaciones)

i_aum = variaciones.index(mayor_aumento)
i_des = variaciones.index(mayor_descenso)

print(f"Mayor aumento: {mayor_aumento} °C entre {fechas[i_aum]} y {fechas[i_aum+1]}")
print(f"Mayor descenso: {mayor_descenso} °C entre {fechas[i_des]} y {fechas[i_des+1]}")
media_movil = [round(statistics.mean(medias[i:i+3]), 2) for i in range(len(medias) - 2)]

# Se asigna al día central de cada ventana (fechas[1] a fechas[-2])
for fecha, original, suavizada in zip(fechas[1:-1], medias[1:-1], media_movil):
    print(f"{fecha}  original: {original:>5}  media móvil: {suavizada:>5}")
#8.4 Calcula una media móvil de tres días y compárala con los valores originales.
media_movil = [round(statistics.mean(medias[i:i+3]), 2) for i in range(len(medias) - 2)]

# Se asigna al día central de cada ventana (fechas[1] a fechas[-2])
for fecha, original, suavizada in zip(fechas[1:-1], medias[1:-1], media_movil):
    print(f"{fecha}  original: {original:>5}  media móvil: {suavizada:>5}")
#8.5 Divide el periodo en semanas y calcula la media de cada una.
for inicio in range(0, len(medias), 7):
    bloque = medias[inicio:inicio + 7]
    fin = inicio + len(bloque) - 1
    print(f"Semana {inicio // 7 + 1} ({fechas[inicio]} a {fechas[fin]}): "
          f"{round(statistics.mean(bloque), 2)} °C")
import pandas as pd
import matplotlib.pyplot as plt
#Las temperaturas por sí solas son solo números: sin la fecha no sabemos a qué día pertenece cada una. Conservar las fechas permite identificar cuándo ocurrió el mayor aumento o descenso, filtrar periodos concretos (semanas, quincenas), comparar tramos del mes y ver la evolución en el tiempo. Además, las listas de fechas y temperaturas están emparejadas por posición, así que si ordenáramos solo las temperaturas perderíamos esa correspondencia y los resultados no tendrían sentido.
plt.scatter(minimas, maximas)
plt.xlabel("Temperatura mínima (°C)")
plt.ylabel("Temperatura máxima (°C)")
plt.title("Temperatura mínima vs máxima - Jaén, enero 2025")
plt.grid(True)
plt.show()
#Hacemos el análisis de los datos meteorológicos con Pandas y Matplotlib. Primero, cargamos los datos desde un archivo CSV que contiene las temperaturas medias junto con sus fechas. Luego, mostramos las temperaturas medias junto con sus fechas y filtramos periodos específicos, como la primera semana y la segunda quincena del mes.


df = pd.read_csv("temperaturas.csv", parse_dates=["fecha"])
    #1.Mostrar las temperaturas medias junto con sus fechas:
    
print(" fechas y temperaturas medias")
print(df[["fecha", "temperatura_media"]])

#2 Filtrar periodos(primera semana y segunda quincena)

print(diferencias.index(max(diferencias)) + 1)
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
 



