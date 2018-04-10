import sys
import cv2
import pytesseract
from PIL import Image

print('Python: ', sys.version)
print('opencv: ', cv2.__version__)
print('pytesseract: ', pytesseract.image_to_string(Image.open("images/test.png")))
