import cv2
import numpy as np

BROKEN_PIXEL_THRESHOLD = 127

def load_image(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Изображение не загружено")
    return image


def find_broken_pixels(image):
    broken_pixels = []
    height, width = image.shape
    for y in range(height):
        for x in range(width):
            if image[y, x] > BROKEN_PIXEL_THRESHOLD:
                broken_pixels.append((x, y))
    return broken_pixels


