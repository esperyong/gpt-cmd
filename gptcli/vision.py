import json

import requests


def recognize_image(image_url: str) -> str:
    api_url = "https://vision.googleapis.com/v1/images:annotate"
    api_key = "YOUR_API_KEY"
    headers = {"Content-Type": "application/json"}
    payload = {
        "requests": [
            {
                "image": {"source": {"imageUri": image_url}},
                "features": [{"type": "LABEL_DETECTION"}]
            }
        ]
    }
    response = requests.post(api_url + "?key=" + api_key, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        raise Exception("Failed to recognize image")
    response_data = response.json()
    try:
        description = response_data["responses"][0]["labelAnnotations"][0]["description"]
        return description
    except (KeyError, IndexError):
        raise Exception("Unexpected response format")

def generate_image(prompt: str) -> str:
    api_url = "https://api.openai.com/v1/images/generations"
    api_key = "YOUR_API_KEY"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }
    payload = {
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        raise Exception("Failed to generate image")
    response_data = response.json()
    try:
        image_url = response_data["data"][0]["url"]
        return image_url
    except (KeyError, IndexError):
        raise Exception("Unexpected response format")
