# FastAPI ML Service Template

A clean, production-ready template for deploying machine learning models using **FastAPI**.

This repository demonstrates how to structure an ML inference service with proper separation of concerns — making it scalable, testable, and deployment-ready.

---

## 🚀 Project Overview

This project provides a structured template for serving trained ML models as REST APIs.

It includes:

✔ Model loading logic  
✔ Request/response validation (Pydantic schemas)  
✔ Service layer abstraction  
✔ Config management  
✔ Clean folder architecture  

Designed for:
- ML engineers deploying models
- Backend engineers integrating ML services
- Production-ready inference pipelines

---

## 📂 Project Structure

ml_api/

├── app/

│   ├── main.py

│   ├── schemas.py

│   ├── model.py

│   ├── service.py

│   └── config.py

├── models/

│   └── model.pkl

└── requirements.txt

---

## 🧠 Architecture

Client Request

↓

FastAPI (main.py)

↓

Pydantic Schema Validation

↓

Service Layer

↓

Model Inference

↓

JSON Response

---

This separation ensures:
- Maintainability
- Testability
- Scalability
- Clean code practices

---

## 🛠️ Tech Stack

- Python 3.8+
- FastAPI
- Pydantic
- Uvicorn
- scikit-learn (or compatible ML model)
- Pickle / Joblib

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-ml-service-template.git
cd fastapi-ml-service-template
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Run the API Server

Start the FastAPI application:
```
uvicorn app.main:app --reload
```

Server runs at:
```
http://127.0.0.1:8000
```

Interactive API docs available at:
```
http://127.0.0.1:8000/docs
```
## Example Request

Example POST request:
```
{
  "features":[7, 71, 1, 8, 5]
}
```
Example response:
```
{
  "prediction": 63.6349091
}
```

---

## 🔧 How to Replace the Model

Train your model.

Save it as:
```
import joblib
joblib.dump(model, open("models/model.pkl", "wb"))
```

Ensure model.py loads it correctly.

Update schema fields if needed.
