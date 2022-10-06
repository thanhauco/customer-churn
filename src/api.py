from fastapi import FastAPI
import pickle
app = FastAPI()
@app.post('/predict')
def predict(data: dict):
    return {'churn': 0}