import argparse
import sys

from gptcli.vision import VisionAPIHandler


def cli_generate_image():
    parser = argparse.ArgumentParser(description="Generate images from prompts.")
    parser.add_argument("prompt", type=str, help="Prompt for generating images.")
    parser.add_argument("--n_images", type=int, default=1, help="Number of images to generate.")
    args = parser.parse_args()

    try:
        vision_handler = VisionAPIHandler(api_key="Your_API_Key_Here")
        response = vision_handler.generate_image(prompt=args.prompt, n_images=args.n_images)
        for image_data in response["data"]:
            print(f"Generated Image URL: {image_data['url']}")
    except Exception as e:
        print(f"Error generating image: {e}")
        sys.exit(1)

def cli_recognize_image():
    parser = argparse.ArgumentParser(description="Recognize text from an image.")
    parser.add_argument("image_path", type=str, help="Path to the image file.")
    args = parser.parse_args()

    try:
        vision_handler = VisionAPIHandler(api_key="Your_API_Key_Here")
        response = vision_handler.recognize_image(image_path=args.image_path)
        print(f"Recognized Text: {response['data']['text']}")
    except Exception as e:
        print(f"Error recognizing image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI for image recognition and generation.")
    parser.add_argument("--generate", action="store_true", help="Generate images from prompts.")
    parser.add_argument("--recognize", action="store_true", help="Recognize text from an image.")
    args = parser.parse_args()

    if args.generate:
        cli_generate_image()
    elif args.recognize:
        cli_recognize_image()
    else:
        parser.print_help()
