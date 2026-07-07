# DATOS: 
# Nombre: Ortega Plaza Diego
# Cuatrimestre:6to
# Carrera :Ing. Desarrollo de Software
# Matricula: 2403230009

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from data.animes import animes

app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/animes")
def get_animes():
    """Devuelve la lista de animes."""
    return [a.to_dict() for a in animes]

@app.get("/animes/{anime_id}")
def get_anime(anime_id: int):
    """Devuelve un solo anime por id."""
    for a in animes:
        if a.id == anime_id:
            return a.to_dict()
    raise HTTPException(status_code=404, detail="Anime no encontrado")

# uvicorn main:app --reload