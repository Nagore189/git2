#pip install fastapi uvicorn

#Instala la biblioteca FastAPI, que se utiliza para crear APIs web rápidas y eficientes.
# APIs web : son interfaces que permiten a las aplicaciones comunicarse entre sí a través de Internet.
#uvicorn : Es un servidor web que se utiliza para ejecutar aplicaciones web basadas en ASGI (Asynchronous Server Gateway Interface).

#Uvicorn es un servidor que ejecuta aplicaciones web basadas en ASGI, como las que se crean con FastAPI. 
#aplicaciones web basadas en ASGI : Son aplicaciones que usan esta interfaz para manejar solicitudes y respuestas.
#Se llaman "asíncronas" porque pueden manejar muchas solicitudes al mismo tiempo de manera eficiente.
# Uvicorn : Es el servidor que se encargará de procesar las solicitudes HTTP y enviar respuestas.


from fastapi import FastAPI
import uvicorn



app= FastAPI() #crea una instancia de FastAPI

@app.get("/") #decorador que indica que la función read_root() se ejecutará cuando se realice una solicitud GET a la raíz de la aplicación.
async def read_root(): #función que se ejecutará cuando se realice una solicitud GET a la raíz de la aplicación.
    return {"message": "Hello World"}    #devuelve un diccioanrio con un mensaje de saludo. El endpoint devolverá este mensaje como respuesta a la solicitud.
                                         # devuelve un json con el mensaje "Hello World" en un servidor web local en la dirección http://127.0.0.1:8000/
                                         # http://127.0.0.1:8000/ es la dirección predeterminada en la que se ejecuta la aplicación FastAPI.
                                         # http://127.0.0.1:8000/ es el punto final de la aplicación, que es la URL a la que se envían las solicitudes HTTP.
                                         # http://127.0.0.1:8000/ es la dirección de la aplicación en el servidor local.







@app.get("/items/{item_id}") #decorador que indica que la función read_item() se ejecutará cuando se realice una solicitud GET a la ruta /items/{item_id}.
def get_items(item_id: int):
    resultado = item_id *10
    return {"item_id": resultado}  # devuelve el endpoint el valor del parámetro item_id multiplicado por 10.
    #return {"item_id": item_id}


#PS D:\TARTANGA\Git\git2> & C:/Users/izaro/anaconda3/envs/MasterIA/python.exe d:/TARTANGA/Git/git2/fastapi_exe/ejercicio1.py
#@PS D:\TARTANGA\Git\git2> & C:/Users/izaro/anaconda3/envs/MasterIA/python.exe d:/TARTANGA/Git/git2/fastapi_exe/ejercicio1.py
#1- PS D:\TARTANGA\Git\git2> & uvicorn fastapi_exe.ejercicio2:app --reload   Usa este comando para iniciar el servidor
#2- probar en el navegador http://127.0.0.1:8000/items/5

#3-  http://127.0.0.1:8000/docs :  es la dirección de la documentación de la API generada automáticamente por FastAPI.

#4- probar desde el terminal 

# 4. 1 Probar desde Gitbash  con curl
# curl -X 'GET' 'http://127.0.0.1:8000/items/10' -H 'accept: application/json'

# 4.2 Probar desde el terminal Invoke-WebRequest -Uri "http://127.0.0.1:8000/items/10" -Headers @{"accept"="application/json"}  .  Invoke-WebRequest, que es el equivalente de curl en PowerShell.

# https://curlconverter.com/  :  Convertir curl a Invoke-WebRequest


#import requests

#headers = {
#    'accept': 'application/json',
#}

#response = requests.get('http://127.0.0.1:8000/items/10', headers=headers)

from typing import List
from pydantic import BaseModel
