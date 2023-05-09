import os
import time

import numpy as np
import pyautogui
from config import *
import cv2
import pytesseract


def make_screenshot(x1, y1, x2, y2):
    return cv2.cvtColor(np.array(pyautogui.screenshot(region=(x1, y1, x2, y2))), cv2.COLOR_RGB2BGR)

def get_digit(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    # Perform text extraction
    data = pytesseract.image_to_string(invert, lang='eng')

    return data
def get_cells_ocr():
    table = [[1, 1] for i in range(cells_amount[0] * cells_amount[1])]
    time.sleep(4)
    image = make_screenshot(table_left_corner[0], table_left_corner[1], cells_amount[0] * width_one_dot,
                            cells_amount[1] * width_one_dot)
    cv2.imshow("", image)
    cv2.waitKey(0)
    # image = cv2.imread(os.path.join(os.curdir, 'screenshot.png'))

    for i in range(cells_amount[0]):
        for j in range(cells_amount[1]):
            current_cell = [width_one_dot * i, width_one_dot * j]
            cell_with_delta = [current_cell[0] + width_one_dot, current_cell[1] + width_one_dot]
            img = np.copy(
                image[current_cell[1]:cell_with_delta[1], current_cell[0]:cell_with_delta[0], :])

            data = get_digit(img)
            num = int(data)
            table[num - 1] = [i, j]

    return table
