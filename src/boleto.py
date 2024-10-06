from pdf2image import convert_from_path
import pytesseract
import cv2 as cv
import os
from PIL import Image
from time import sleep

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image):
    text = pytesseract.image_to_string(image, lang='por')
    return text

def get_data(image):
    img = cv.imread(image, 1)
    name_picture = img[600:650, 370:1000]#
    value_picture = img[1230:1290, 370:1000]#
    desc_picture = img[1590:1640, 240:1000]#
    name = extract_text(name_picture)[:-1]
    value = extract_text(value_picture)[:-1]
    desc = extract_text(desc_picture)[:-1]
    if value[:3] != "R$ ":
        name_picture = img[640:690, 370:1000]#
        value_picture = img[1270:1320, 370:1000]#
        desc_picture = img[1620:1680, 240:1000]#
        name = extract_text(name_picture)[:-1]
        value = extract_text(value_picture)[:-1]
        desc = extract_text(desc_picture)[:-1]
    if desc[:9] != 'Descrição':
        desc = ''
    else:
        desc = desc[11:]
    data = {'name': name, 'value': value, 'desc': desc}
    return data


path = f'{os.getcwd()}\\COMPROVANTES\\BOLETO'

dump_folder = f'{path}\\dump'

output_folder = f'{os.getcwd()}\\COMPROVANTES\\SEPARADOS'

for file in os.listdir(path):
    if file == 'dump':
        break
    pdf_pages = convert_from_path(f'{path}\\{file}', poppler_path='src/poppler-24.07.0/Library/bin', output_folder=dump_folder, fmt='jpg')

sleep(3)

for item in os.listdir(dump_folder):
    
    img_path = f'{dump_folder}\\{item}'
    data = get_data(img_path)
    name = data['name']
    value = data['value']
    desc = data['desc']

    pdf = Image.open(img_path)
    output_filename = f'{output_folder}\\BOLETO_{name}_{value}_{desc}'

    c = 1

    output_path = output_filename

    while os.path.exists(output_path + ".pdf"):
        output_path = output_filename + f'_{c}'
        c += 1        

    pdf.save(output_path + '.pdf')