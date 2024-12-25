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



#PS D:\TARTANGA\Git\git2> & C:/Users/izaro/anaconda3/envs/MasterIA/python.exe d:/TARTANGA/Git/git2/fastapi_exe/ejercicio1.py
#@PS D:\TARTANGA\Git\git2> & C:/Users/izaro/anaconda3/envs/MasterIA/python.exe d:/TARTANGA/Git/git2/fastapi_exe/ejercicio1.py
#PS D:\TARTANGA\Git\git2> & uvicorn fastapi_exe.ejercicio1:app --reload
