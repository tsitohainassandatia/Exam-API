from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()

@app.get('/ping')
def ping():
    return Response ("pong", status_code=300)