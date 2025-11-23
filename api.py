from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()

# ---------- MODELO ----------
data = pd.DataFrame({
    "distancia_km": [2.1, 5.3, 12.5, 8.0, 1.5, 3.4],
    "clima": ["sol", "chuva", "sol", "nublado", "sol", "chuva"],
    "horario": ["manha", "tarde", "manha", "noite", "manha", "tarde"],
    "modal_recomendado": ["caminhada", "onibus", "carona", "bike", "caminhada", "onibus"]
})

enc_clima = LabelEncoder()
enc_horario = LabelEncoder()
enc_modal = LabelEncoder()

data["clima"] = enc_clima.fit_transform(data["clima"])
data["horario"] = enc_horario.fit_transform(data["horario"])
data["modal_recomendado"] = enc_modal.fit_transform(data["modal_recomendado"])

X = data[["distancia_km", "clima", "horario"]]
y = data["modal_recomendado"]

model = RandomForestClassifier()
model.fit(X, y)

# ---------- API ----------
class Entrada(BaseModel):
    distancia: float
    clima: str
    horario: str

@app.post("/recomendar")
def recomendar_api(entrada: Entrada):
    clima = enc_clima.transform([entrada.clima])[0]
    horario = enc_horario.transform([entrada.horario])[0]

    df = pd.DataFrame([[entrada.distancia, clima, horario]],
                      columns=["distancia_km", "clima", "horario"])

    pred = model.predict(df)
    modal = enc_modal.inverse_transform(pred)[0]

    return {"modal_recomendado": modal}
