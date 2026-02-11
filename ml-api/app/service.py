from .model import ml_model

def run_prediction(features: list[float]) -> float:
    return float(ml_model.predict(features))