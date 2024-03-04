from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
#CORS
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials = True,
        allow_methods=["*"],
        allow_headers=["*"],
)

class SumRequest(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
async def calculate(request: SumRequest):
    result = request.num1 + request.num2
    return {"sum": result}
