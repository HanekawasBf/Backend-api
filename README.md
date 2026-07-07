# AnimeLat - Backend (API REST)

API REST desarrollada con **FastAPI** que provee la información de animes (títulos, imágenes, sinopsis y video) consumida por el frontend de AnimeLat.

- Ortega Plaza Diego
- Matrícula: 240323000
- Proyecto Integrador - 2do Parcial
- Asignatura: Desarrollo Backend I
- 6to Cuatrimestre - Ingeniería en Desarrollo de Software

## Repositorio del Frontend

Este backend trabaja en conjunto con el proyecto de frontend, disponible en:
`https://github.com/HanekawasBf/Frontend-Api`

Ambos proyectos se ejecutan de forma independiente y se comunican mediante peticiones HTTP (API REST).

## Tecnologías

- Python 3
- FastAPI
- Uvicorn (servidor ASGI)
- CORSMiddleware (para permitir peticiones desde el frontend)

## Estructura del proyecto

```
backend/
├── main.py              # Configuración de la app, middleware CORS y rutas
├── models/
│   └── anime.py         # Clase Anime
├── data/
│   └── animes.py        # Lista de instancias de Anime (datos)
└── README.md
```

## Ejecución

### 1. Levantar el servidor

```bash
uvicorn main:app --reload
```

El servidor quedará disponible en:
`http://127.0.0.1:8000`

## Endpoints disponibles

| Método | Ruta               | Descripción                                  |
|--------|--------------------|-----------------------------------------------|
| GET    | `/animes`          | Devuelve la lista completa de animes          |
| GET    | `/animes/{id}`     | Devuelve un solo anime según su id            |

## Configuración de CORS

Los orígenes permitidos actualmente son:

```python
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]
```

Si el frontend corre en un puerto distinto (por ejemplo, si Live Server asigna 5501), debe agregarse a esta lista en `main.py` para evitar errores de política CORS.

## Notas

- Los datos se manejan en memoria a través de la clase `Anime`.
- Backend y frontend deben ejecutarse **al mismo tiempo** en terminales/ventanas separadas para que la comunicación por `fetch()` funcione correctamente.
