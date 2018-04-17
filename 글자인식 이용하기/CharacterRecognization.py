from PIL import Image
import pytesseract

def ocr_tesseract():
    image_file = "../images/scannedImage.png"
    im = Image.open(image_file)
    text = pytesseract.image_to_string(im)
    im.show()
    print(text)

if __name__ == "__main__":
    ocr_tesseract()