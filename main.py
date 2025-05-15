from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola, tu API de FastAPI ya está funcionando en Railway"}

@app.get("/buscar-banda")
def buscar_banda(nombre_banda: str):
    return {"banda": nombre_banda, "resultado": "Aquí iría la búsqueda en Metal Archives"}
