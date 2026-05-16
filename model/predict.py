import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def predict_price(features):
    features = np.array(features).reshape(1, -1)
    return float(model.predict(features)[0])
