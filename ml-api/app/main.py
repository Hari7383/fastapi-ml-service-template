from fastapi import FastAPI, HTTPException # type: ignore
from .schemas import PredictionInput, PredictionOutput
from .service import run_prediction

app = FastAPI(title="ML Inference API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: PredictionInput):
    try:
        result = run_prediction(data.features)
        return PredictionOutput(prediction=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
