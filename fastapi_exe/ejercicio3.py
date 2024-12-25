
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Food(BaseModel):   
   """
   BaseModel Se utiliza para definir modelos de datos.
   Un modelo de datos es como una plantilla que asegura que los datos que entran o salen de tu aplicación sigan un formato específico.
    Este modelo representa un plato de comida.
    Atributos:
        name (str): El nombre del plato.
        ingredients (List[str]): Una lista de ingredientes para el plato.
    """
   name: str
   ingredients: List[str]

@app.post("/food/") #Define un endpoint en la ruta /food/ que acepta solicitudes HTTP de tipo POST.
                    # Cuando alguien envíe datos a /food/, se ejecutará la función prepare_food.
                    #estamos enviando un json con el nombre y los ingredientes del plato de comida.
def prepare_food(food: Food, delivery: bool = False): #La función prepare_food() toma un parámetro food de tipo Food y un parámetro delivery de tipo bool.
    return {"message": f"preparing {food.name}, ingredientes {food.ingredients} ",   "delivery": delivery} #devuelve un diccionario con un mensaje que indica que se está preparando el plato de comida y si se va a entregar a domicilio.

# Parámetros de la función:
# food: Food: El cuerpo de la solicitud (JSON) debe coincidir con el modelo Food.
# delivery: bool = False: Parámetro opcional que indica si el plato será entregado a domicilio.

# Respuesta:
# Devuelve un diccionario con un mensaje y el valor del parámetro delivery.


# 5. Ejecutar el Servidor
# Para que este archivo .py funcione como servidor, lo ejecutas con Uvicorn:
# uvicorn nombre_archivo:app --reload
# nombre_archivo: Es el nombre del archivo .py donde está el código (sin la extensión .py).
# app: Es la instancia de FastAPI que definiste.

# Tu archivo .py es un servidor web hecho con FastAPI.
# Este servidor:
# Recibe solicitudes HTTP (como POST).
# Valida los datos enviados usando BaseModel.
# Responde con un mensaje JSON que puede ser entendido por otros programas.

   


#1- PS D:\TARTANGA\Git\git2> & uvicorn fastapi_exe.ejercicio2:app --reload   Usa este comando para iniciar el servidor
#2- probar en el navegador http://127.0.0.1:8000/food/  :  es la dirección de la API que acabamos de crear.


# import requests   # es una biblioteca de Python que se utiliza para hacer solicitudes HTTP (como GET, POST, etc.).

# headers = {   # Son metadatos que acompañan a la solicitud HTTP para proporcionar información adicional.
#     'accept': 'application/json',  # Indica que el cliente (tu programa) espera recibir una respuesta en formato JSON.
#     'Content-Type': 'application/json', #Especifica que el cuerpo de la solicitud contiene datos en formato JSON.
# }

# params = {
#     'delivery': 'false',   # Los parámetros de consulta (query parameters) se agregan a la URL en formato clave=valor. Los parámetros generalmente se usan para enviar información adicional al servidor.
# }

# json_data = {
#     'name': 'nachos',
#     'ingredients': [
#         'patatas',
#         'queso',
#     ],
# }

# response = requests.post('http://127.0.0.1:8000/food/', params=params, headers=headers, json=json_data)
