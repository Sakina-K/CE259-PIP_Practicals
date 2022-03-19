#20CE046 SAKINA KUTERWADLI
#PRACTICAL 10
#Creating a pdf file for sem 3 result
#   Github Repository link: https://github.com/Sakina-K/CE259-PIP_Practicals.git

import img2pdf
from PIL import Image
import os

#storing img path
img_path="C:/Users/User/Desktop/lab/result.png"

#storing pdf path
pdf_path="C:/Users/User/Desktop/lab/practical10.pdf"

#opening image
image=Image.open(img_path)

#converting into chunks
pdf_bytes=img2pdf.convert(image.filename)

#opening file
file=open(pdf_path,"wb")

#writing pdf file with chunks
file.write(pdf_bytes)

#closing image and file
image.close()
file.close()

print("done")