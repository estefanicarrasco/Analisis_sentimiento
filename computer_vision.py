import streamlit as st
import requests

st.set_page_config(page_title="Análisis de texto", page_icon="🧠")

st.title("🧠 Analizador de Sentimiento y Lenguaje")
st.markdown("Escribe un texto y analizaremos su idioma y sentimiento usando Azure Cognitive Services.")

# Entradas
user_input = st.text_area("✍️ Escribe tu texto aquí")

if st.button("Analizar"):
    if not user_input:
        st.warning("Por favor, ingresa un texto.")
    else:
        endpoint = st.secrets["AZURE_TEXT_ENDPOINT"]
        key = st.secrets["AZURE_TEXT_API_KEY"]
        url = endpoint + "/text/analytics/v3.1/analyze"

        headers = {
            "Ocp-Apim-Subscription-Key": key,
            "Content-Type": "application/json"
        }

        payload = {
            "kind": "SentimentAnalysis",
            "parameters": {
                "modelVersion": "latest"
            },
            "analysisInput": {
                "documents": [
                    {"id": "1", "language": "es", "text": user_input}
                ]
            }
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            sentiment = result['results']['documents'][0]['sentiment']
            confidence = result['results']['documents'][0]['confidenceScores']
            st.success(f"✅ Sentimiento detectado: **{sentiment.upper()}**")
            st.write("Confianza del modelo:")
            st.json(confidence)
        else:
            st.error("Ocurrió un error al conectar con la API")
            st.text(response.json())

