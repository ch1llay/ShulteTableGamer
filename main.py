import os.path

import pytesseract

import OCR

if __name__ == "__main__":
   # pytesseract.pytesseract.tesseract_cmd = os.path.join(os.curdir, "pytesseract.exe")
    table = OCR.get_cells_ocr()