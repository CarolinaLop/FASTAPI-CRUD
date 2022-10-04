#Ver el tutorial https://cosasdedevs.com/posts/conexion-base-datos-modelos-fastapi/
import py_compile
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def home():
    return {"message": "Hello World"}
