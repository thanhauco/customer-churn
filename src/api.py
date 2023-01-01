from fastapi import FastAPI, HTTPException
@app.post('/predict')
def predict(data: dict):
    if 'age' not in data: raise HTTPException(400)
    return {'churn': 0}