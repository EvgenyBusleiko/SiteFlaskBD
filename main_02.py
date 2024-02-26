import random

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


movies = []

for i in range(10):
    movie = Movie(
        id=random.randint(0, 5),
        title=f'{random.randint(0, 5)}',
        description=f'{random.randint(0, 5)}',
        genre=random.randint(0, 5))
    movies.append(task)


@app.get('/')
async def root():
    return movies


@app.post('/task/')
async def create_movie(movie: Movies):
    movies.append(movie)
    return movies


@app.get("/put/")
async def get_movie_by_genge(genre_new:string, movie: Movie):
    result=[]
    for movie in movies:
        if movie.genre == genre_new:
            result.append(movie)
            return result
    return {"message": "Movies not found"}


# @app.delete("/delete/")
# async def delete_task(task_id: str, movie: Movie):
#     for t in tasks:
#         if t.id == task.id:
#             tasks.remove(t)
#             return {"message": "Movie removed"}
#     return {"message": "Movies not found"}