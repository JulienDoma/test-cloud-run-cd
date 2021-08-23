from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "Hello from Cloud Run CD"


@app.get("/addition")
def addition(first, second):
    first = int(first)
    second = int(second)
    res = first + second
    return f"{first} + {second} = {res}"