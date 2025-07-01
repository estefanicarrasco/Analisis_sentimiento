import streamlit as st
import requests

st.set_page_config(page_title="Analizador de Sentimientos", page_icon="💬")

# Encabezado
st.title("💬 Analizador de Sentimientos con Azure")
st.markdown("Escribe un texto en español y detectaremos si es positivo, neutral o negativo usando **Azure Cognitive Services**.")

# API Key y Endpoint desde Secrets
API_KEY = st.secrets["AZURE_TEXT_API_KEY"]
ENDPOINT = st.secrets["AZURE_TEXT_ENDPOINT"]

# Headers para autenticación
headers = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "Content-Type": "application/json"
}

# Función para analizar sentimiento
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

# Text input
texto_usuario = st.text_area("✍️ Escribe tu texto aquí:")

if st.button("🔍 Analizar"):
    if texto_usuario.strip() == "":
        st.warning("Por favor, escribe algo para analizar.")
    else:
        resultado = analizar_sentimiento(texto_usuario)

        if "error" in resultado:
            st.error("❌ Ocurrió un error al procesar el texto.")
            st.json(resultado)
        else:
            sentimiento = resultado["documents"][0]["sentiment"]
            confianza = resultado["documents"][0]["confidenceScores"]

            st.success(f"📌 Sentimiento detectado: **{sentimiento.upper()}**")
            st.write("🔢 Confianza:")
            st.json(confianza)

