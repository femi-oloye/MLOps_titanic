from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("./model/titanic_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define request body structure
class Passenger(BaseModel):
    Pclass: int
    Sex: int  # 1 for male, 0 for female
    Age: float
    Fare: float

@app.get("/")
def home():
    return {"message": "Titanic Survival Prediction API"}

@app.post("/predict")
def predict(passenger: Passenger):
    """Predict survival based on passenger details"""
    data = np.array([[passenger.Pclass, passenger.Sex, passenger.Age, passenger.Fare]])
    prediction = model.predict(data)
    return {"Survived": int(prediction[0])}
