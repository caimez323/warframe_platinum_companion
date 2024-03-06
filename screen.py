import cv2, pyautogui, pytesseract

from PIL import Image
import numpy as np


TESSERACT_PATH = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"



def screen_analysis(x1,y1,x2,y2):
# Spécifiez les coordonnées du coin supérieur gauche et inférieur droit de la zone à capturer
    #x1, y1, x2, y2 = 475, 200, 1450, 600
    #x1, y1, x2, y2 = 475, 387, 1450, 459
    #x1, y1, x2, y2 = 475, 387, 1450, 520

    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    # Screenshot from coordonates with OpenCV
    screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Convert picture
    gray_image = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    negative_image= cv2.bitwise_not(gray_image)

    # Save picture
    cv2.imwrite('preprocessed_negative.png', negative_image)

    # Read picture
    negative_text = pytesseract.image_to_string(Image.open('preprocessed_negative.png'))

    # Print text
    #print("negative")
    #print(negative_text)

    # Display picture
    #cv2.imshow('Original Image', screenshot)
    # cv2.imshow('Preprocessed negative', negative_image)

    return negative_text



