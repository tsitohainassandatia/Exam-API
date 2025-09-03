from fastapi import FastAPI
from starlette.responses import Response
from starlette.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

#question 1
# a-
@app.get('/health')
def ping():
    return Response ("OK")

# b-
class phone(BaseModel):
    identifiant: str
    brand: str
    model: str


@app.post("/phones")
def post_phone(request: phone):
    return JSONResponse({request.identifiant},{request.brand}, {request.model}, status_code=201)
