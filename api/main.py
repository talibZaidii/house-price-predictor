from fastapi import FastAPI
from pydantic import BaseModel
from model.predict import predict_price

app = FastAPI()


class House(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/predict")
def predict(house: House):
    features = [
        house.longitude,
        house.latitude,
        house.housing_median_age,
        house.total_rooms,
        house.total_bedrooms,
        house.population,
        house.households,
        house.median_income,
    ]

    return {
        "predicted_price": predict_price(features)
    }
