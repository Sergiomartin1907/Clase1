#Importar Fastapi
from fastapi import FastAPI

#Crear una instancia de FastAPI
app = FastAPI()

#Definir una ruta de ejemplo
@app.get("/ping")
def ping():
    return {"message": "pong"}

#Ejecutar la aplicación
@app.get("/")
def Holla_mundo():
    return {"message": "Holla Mundo"}

@app.get("/Sergio")
def Sergio():
    return {"Nicole"}

