from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict


app = FastAPI()

class PredictionOutput(BaseModel):
    prediction: str

class PredictionRequestBody(BaseModel):
    pict: str

@app.get('/')
def health_check():
    return {'health_check': 'OK'}

@app.post('/predict', response_model=PredictionOutput)
def predict_post(payload:PredictionRequestBody):
    prediction = predict(payload.pict)
    return {'prediction': str(prediction)}