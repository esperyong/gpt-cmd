import json

import requests
from PIL import Image


def recognize_image(image_path):
    api_url = "https://api.openai.com/v1/clip"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    with open(image_path, "rb") as image_file:
        response = requests.post(api_url, headers=headers, files={"file": image_file})
    response.raise_for_status()
    return json.loads(response.text)["text"]

def generate_image(prompt):
    api_url = "https://api.openai.com/v1/dalle"
    headers = {"Authorization": "Bearer YOUR_API_KEY", "Content-Type": "application/json"}
    data = {"prompt": prompt}
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    image_data = json.loads(response.text)["image_data"]
    image = Image.open(image_data)
    image.save(f"{prompt[:10]}.png")
