from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

endpoint = "https://<TU_ENDPOINT>.cognitiveservices.azure.com/"
key = "<TU_API_KEY>"

client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

# Analiza una imagen desde una URL
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Shaki_waterfall.jpg/800px-Shaki_waterfall.jpg"
features = ["description", "tags"]

analysis = client.analyze_image(image_url, visual_features=features)

for caption in analysis.description.captions:
    print(f"Descripción: '{caption.text}' con confianza {caption.confidence:.2f}")


