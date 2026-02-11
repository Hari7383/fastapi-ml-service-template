import joblib # type: ignore
from .config import settings

class MLModel:
    def __init__(self):
        self.model = self._load_model()

    def _load_model(self):
        return joblib.load(settings.MODEL_PATH)

    def predict(self, features):
        return self.model.predict([features])[0]

ml_model = MLModel()
