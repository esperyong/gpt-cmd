import base64
import json

import aiohttp


class VisionAPIHandler:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {api_key}"}

    async def generate_image(self, prompt: str, n_images: int = 1):
        async with aiohttp.ClientSession() as session:
            payload = {"prompt": prompt, "n": n_images}
            async with session.post("https://api.openai.com/v1/images/generations", headers=self.headers, json=payload) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Failed to generate image: {response.status}")

    async def recognize_image(self, image_path: str):
        image_base64 = encode_image_to_base64(image_path)
        async with aiohttp.ClientSession() as session:
            payload = {"image": image_base64}
            async with session.post("https://api.openai.com/v1/vision/recognitions", headers=self.headers, json=payload) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Failed to recognize image: {response.status}")

def encode_image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def decode_base64_to_image(base64_str: str, output_path: str):
    with open(output_path, "wb") as output_file:
        output_file.write(base64.b64decode(base64_str))

def decode_response_to_text(response: dict) -> str:
    return response.get("data", {}).get("text", "")
