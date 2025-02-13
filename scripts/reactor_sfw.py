from transformers import pipeline
from PIL import Image
import logging

SCORE = 2.00

logging.getLogger('transformers').setLevel(logging.ERROR)

def nsfw_image(img_path: str, model_path: str):
    return False  # Always return False (no filtering)

