import random
from random import choice

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


movies = []
genres = ["Ужас", "Триллер", "Комедия", "Исторический", "Фантастика"]
for i in range(1, 11):
    new_movie = Movie(
        id=i,
        title=f"title{i}",
        description=f"description{i}",
        genre=choice(genres)
    )
    movies.append(new_movie)


@app.get("/movies/")
async def get_movies():
    return movies


@app.get("/movies/{genre}")
async def get_movies_by_genre(genre: str):
    result = []
    for movie in movies:
        if movie.genre == genre:
            result.append(movie)
    return result if result else {"message": "No movies in that genre"}


@app.post("/movies/")
async def create_movie(movie: Movie):
    movies.append(movie)
    return movie


@app.put("/movies/")
async def update_movie(movie_id: int, movie: Movie):
    for i, m in enumerate(movies):
        if m.id == movie_id:
            movies[i] = movie
            return movie
    return {"message": "movie not found"}


@app.delete("/movie/")
async def delete_movie(movie_id: int):
    for movie in movies:
        if movie.id == movie_id:
            movies.remove(movie)
            return {"message": "movie removed"}
    return {"message": "movie not found"}

# class Task(BaseModel):
#     id: int
#     title: str
#     description: str
#     status: int
#
#
# tasks = []
#
# for i in range(10):
#     task = Task(
#         id=random.randint(0, 5),
#         title=f'{random.randint(0, 5)}',
#         description=f'{random.randint(0, 5)}',
#         status=random.randint(0, 5))
#     tasks.append(task)
#
#
# @app.get('/')
# async def root():
#     return tasks
#
#
# @app.post('/task/')
# async def create_task(task: Task):
#     tasks.append(task)
#     return tasks
#
#
# @app.put("/put/")
# async def update_task(task_id: int, task: Task):
#     for t in tasks:
#         if t.id == task.id:
#             t = task
#             return task
#     return {"message": "Task not found"}
#
#
# @app.delete("/delete/")
# async def delete_task(task_id: int, task: Task):
#     for t in tasks:
#         if t.id == task.id:
#             tasks.remove(t)
#             return {"message": "Task removed"}
#     return {"message": "Task not found"}
