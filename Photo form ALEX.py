import cv2
import numpy as np

MAX_DISTANCE = 10
DISTANCE_DIFFERENCE_THRESHOLD = 3
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


def find_horizontal_neighbors(x, y, image):
    left = None
    right = None


    for dx in range(1, MAX_DISTANCE + 1):
        if x - dx < 0:
            break
        if image[y, x - dx] <= BROKEN_PIXEL_THRESHOLD:
            left = (x - dx, y)
            break

    for dx in range(1, MAX_DISTANCE + 1):
        if x + dx >= image.shape[1]:
            break
        if image[y, x + dx] <= BROKEN_PIXEL_THRESHOLD:
            right = (x + dx, y)
            break

    return left, right


def find_vertical_neighbors(x, y, image):
    up = None
    down = None

    for dy in range(1, MAX_DISTANCE + 1):
        if y - dy < 0:
            break
        if image[y - dy, x] <= BROKEN_PIXEL_THRESHOLD:
            up = (x, y - dy)
            break

    for dy in range(1, MAX_DISTANCE + 1):
        if y + dy >= image.shape[0]:
            break
        if image[y + dy, x] <= BROKEN_PIXEL_THRESHOLD:
            down = (x, y + dy)
            break

    return up, down

