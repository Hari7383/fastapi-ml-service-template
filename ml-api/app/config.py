from pydantic_settings import BaseSettings # type: ignore

class Settings(BaseSettings):
    MODEL_PATH: str = "E:\\VS_Programs\\fastapi\\ml-api\\models\\student_performance_model.pkl"

settings = Settings()
