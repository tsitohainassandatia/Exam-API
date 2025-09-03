from fastapi import FastAPI
from starlette.responses import Response
from starlette.responses import JSONResponse

app = FastAPI()

#question 1
# a-
@app.get('/health')
def ping():
    return Response ("OK")

# b-
@app.post('/phones')
def phones(id: str = "non defini"):
    return JSONResponse( {id},status_code=201)