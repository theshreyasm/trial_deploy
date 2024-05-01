import requests
import json
import base64

image_path="captured_image.png"

def generate(image_path):

    # with open(image_path,'rb') as image_file:
    #     image_base64=base64.b64encode(image_file.read()).decode('utf-8')

    with open(image_path, "rb") as f:
        data = f.read()

    url = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(url, headers=headers, data=data)

    output = response.json()
    text = output[0]["generated_text"]

    return text