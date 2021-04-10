
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
from pdf2image.exceptions import( PDFInfoNotInstalledError,PDFPageCountError, PDFSyntaxError )

pytesseract.pytesseract.tesseract_cmd = r'X:\New folder'
PDF_file = "D:\\Pega notes\\Pega academy IA1\\Ruesets.pdf"
  
# Store all the pages of the PDF in a variable
pages = convert_from_path(PDF_file, 500, poppler_path=r'C:\Users\Varssha\Downloads\poppler-0.68.0_x86\poppler-0.68.0\bin')
  
# Counter to store images of each page of PDF to image
image_counter = 1
  
for page in pages:
  
    filename = "page_"+str(image_counter)+".jpg"
      
    # Save the image of the page in system
    page.save(filename, 'JPEG')

    image_counter = image_counter + 1
  
filelimit = image_counter-1
  
outfile = "out_text.txt"
  
f = open(outfile, "a")
  
# Iterate from 1 to total number of pages
for i in range(1, filelimit + 1):
  
    filename = "page_"+str(i)+".jpg"
          
    # Recognize the text as string in image using pytesserct
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    text = text.replace('-\n', '')    
  
    # Finally, write the processed text to the file.
    f.write(text)
  
# Close the file after writing all the text.
f.close()