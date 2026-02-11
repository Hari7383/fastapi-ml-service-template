from pydantic import BaseModel, Field # type: ignore
from typing import List

class PredictionInput(BaseModel):
    features: List[float] = Field(..., min_items=1)

class PredictionOutput(BaseModel):
    prediction: float
