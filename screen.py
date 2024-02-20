import cv2
import pyautogui
import pytesseract
from PIL import Image
import numpy as np


def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)

# Spécifiez les coordonnées du coin supérieur gauche et inférieur droit de la zone à capturer
x1, y1, x2, y2 = 475, 387, 1450, 459
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Clément\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# Capture d'écran de la zone spécifiée avec OpenCV
screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Convertissez l'image en niveaux de gris
gray_image = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
negative_image= cv2.bitwise_not(gray_image)
# Appliquez un flou gaussien pour réduire le bruit
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

noise_remove = noise_removal(blurred_image)

# Appliquez un seuillage adaptatif pour binariser l'image
thresh_image = cv2.threshold(noise_remove, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

# Appliquez une opération de dilation pour connecter les composants du texte
kernel = np.ones((3, 3), np.uint8)
dilated_image = cv2.dilate(thresh_image, kernel, iterations=1)

# Enregistrez l'image temporaire après prétraitement
cv2.imwrite('preprocessed_negative.png', negative_image)
cv2.imwrite('preprocessed_blur.png', blurred_image)
cv2.imwrite('preprocessed_thresh_dilate.png', dilated_image)

# Utilisez pytesseract pour extraire le texte de l'image prétraitée
extracted_text = pytesseract.image_to_string(Image.open('preprocessed_thresh_dilate.png'))

# Affiche l'image originale
cv2.imshow('Original Image', screenshot)

# Affiche l'image prétraitée
cv2.imshow('Preprocessed dilated', dilated_image)
cv2.imshow('Preprocessed negative', negative_image)
cv2.imshow('Preprocessed blur', blurred_image)

# Affiche le texte extrait
print("Texte extrait de l'écran :")
print(extracted_text)
print("blur")
print(pytesseract.image_to_string(Image.open('preprocessed_blur.png')))
print("negative")
print(pytesseract.image_to_string(Image.open('preprocessed_negative.png')))

# Attendez une touche et fermez les fenêtres d'affichage
cv2.waitKey(0)
cv2.destroyAllWindows()
