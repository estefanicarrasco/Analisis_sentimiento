import requests
import streamlit as st

# API keys (guardadas con st.secrets en producción)
API_KEY = st.secrets["AZURE_TEXT_API_KEY"]
ENDPOINT = st.secrets["AZURE_TEXT_ENDPOINT"]

headers = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "Content-Type": "application/json"
}

def analizar_sentimiento(texto):
    data = {
        "documents": [
            {
                "language": "es",
                "id": "1",
                "text": texto
            }
        ]
    }
    url = f"{ENDPOINT}/text/analytics/v3.0/sentiment"
    response = requests.post(url, headers=headers, json=data)
    return response.json()

st.title("🔍 Analizador de Sentimiento con Azure")

texto = st.text_area("Escribe un texto para analizar el sentimiento")

if st.button("Analizar"):
    resultado = analizar_sentimiento(texto)
    sentimiento = resultado['documents'][0]['sentiment']
    st.write(f"💬 El sentimiento detectado es: **{sentimiento.upper()}**")

