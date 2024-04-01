import re
from pdf2image import convert_from_path
from pytesseract import image_to_string
# from pypdf import PdfReader

# reader = PdfReader("/home/fawzan/Fawzan/PT/RajaYogamBySwamiVivekanandamalayalamTranslationByKumaranAsan.pdf")
# number_of_pages = len(reader.pages)
# page = reader.pages[5]
# text = page.extract_text()

images = convert_from_path('Indian Penal Code Book.pdf')

text = image_to_string(images[5])


# text_content = " ".join(re.findall(r'[\u0D00-\u0D7F]+',text))
# text_content = " ".join(re.findall(r'[\u0D00-\u0D7F]+',text))

# print(text_content)
print(text)