import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model():
    data = pd.read_csv("data.csv")

    X = data[["temperature", "humidity", "rainfall"]]
    y = data["disease"]

    model = RandomForestClassifier()
    model.fit(X, y)

    pickle.dump(model, open("model.pkl", "wb"))

def load_model():
    return pickle.load(open("model.pkl", "rb"))

def predict_risk(model, temp, humidity, rainfall):
    pred = model.predict_proba([[temp, humidity, rainfall]])[0][1]
    return pred
