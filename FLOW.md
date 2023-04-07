## ToDo

1. ***Merge PDF***
```
from pypdf import PdfMerger

pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
```
---
2. ***Split PDF***
```

from PyPDF2 import PdfWriter, PdfReader

inputpdf = PdfReader(open("document.pdf", "rb"))

for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)

```
---
3. ***PDF to Word***
```
import aspose.words as aw

doc = aw.Document("Input.pdf")
doc.save("Output.docx")
```
---
4. ***PDF to Powerpoint***
```
import aspose.slides as slides
import aspose.pydrawing as drawing
        
with slides.Presentation() as pres:
    pres.slides.add_from_pdf("document.pdf")
    pres.save("OutputPresentation.ppt", slides.export.SaveFormat.PPT)
```
---
5. ***PDF to Excel***
```
Steps: Convert PDF to XLS in Python

    Create an instance of Document object with the source PDF document.
    Create an instance of ExcelSaveOptions.
    Save it to XLS format specifying .xls extension by calling Document.Save() method and passing it ExcelSaveOptions.


    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xls.xls"
    # Open PDF document
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003

    # Save the file into MS Excel format
    document.save(output_pdf, save_option)

```
```
Steps: Convert PDF to XLSX in Python

    Create an instance of Document object with the source PDF document.
    Create an instance of ExcelSaveOptions.
    Save it to XLSX format specifying .xlsx extension by calling Document.Save() method and passing it ExcelSaveOptions.


    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_xlsx.xlsx"
    # Open PDF document
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()

    # Save the file into MS Excel format
    document.save(output_pdf, save_option)

```
---
6. ***Excel to PDF***
```
Aspose.Cells - Converting Excel To Pdf

To convert Excel to Pdf file using Aspose.Cells for Java in Python, simply invoke excel_to_pdf() method of Converter module.

Python Code

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."
```
---
7. ***Word to PDF***
```
import aspose.words as aw

# Load word document
doc = aw.Document("calibre.docx")

# Create save options and set compliance
saveOptions = aw.saving.PdfSaveOptions()
saveOptions.compliance = aw.saving.PdfCompliance.PDF17 

# Save as PDF
doc.save("PDF.pdf", saveOptions)
```
---
8. ***Powerpoint to PDF***
```
import aspose.slides as slides

# Load presentation
pres = slides.Presentation("presentation.pptx")

# Convert PPTX to PDF
pres.save("pptx-to-pdf.pdf", slides.export.SaveFormat.PDF)
```
---
9. ***PDF to JPG***
```
from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('example.pdf')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
```
---
10. ***JPG to PDF***
```
from PIL import Image

image_1 = Image.open(r'path where the image is stored\file name.png')
im_1 = image_1.convert('RGB')
im_1.save(r'path where the pdf will be stored\new file name.pdf')
```
---
11. ***Watermark***
```
# import all the libraries
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np
 
# image opening
image = Image.open("puppy.jpg")
# this open the photo viewer
image.show() 
plt.imshow(image)
 
# text Watermark
watermark_image = image.copy()
 
draw = ImageDraw.Draw(watermark_image)
# ("font type",font size)
w, h = image.size
x, y = int(w / 2), int(h / 2)
if x > y:
  font_size = y
elif y > x:
  font_size = x
else:
  font_size = x
   
font = ImageFont.truetype("arial.ttf", int(font_size/6))
 
# add Watermark
# (0,0,0)-black color text
draw.text((x, y), "puppy", fill=(0, 0, 0), font=font, anchor='ms')
plt.subplot(1, 2, 1)
plt.title("black text")
plt.imshow(watermark_image)
 
# add Watermark
# (255,255,255)-White color text
draw.text((x, y), "puppy", fill=(255, 255, 255), font=font, anchor='ms')
plt.subplot(1, 2, 2)
plt.title("white text")
plt.imshow(watermark_image)

```
---
12. ***HTML to PDF***
```
import pdfkit
pdfkit.from_file('test.html', 'out.pdf')
pdfkit.from_url('https://www.google.co.in/','shaurya.pdf')
pdfkit.from_string('Shaurya GFG','GfG.pdf')

pdfkit.from_url(['google.com', 'geeksforgeeks.org', 'facebook.com'], 'shaurya.pdf')
pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf')

```
---
13. ***Unlock PDF***
```
import pikepdf

pdf_loc = input("PDF location: ")
pdf_pass = input("PDF password: ")

pdf = pikepdf.open(pdf_loc, password=pdf_pass)

print("\nProcessing...\n")

pdf_save = input("Save file as: ")
pdf_loc2 = input("Save location: ")

pdf.save(pdf_loc2 + '\\' + pdf_save)

print("The password successfully removed from the PDF")
print("\aLocation: " + pdf_loc + '\\' + pdf_save)
```
---
14. ***Protect PDF***
```

from PyPDF2 import PdfReader, PdfWriter
reader = PdfReader("WBW3.pdf")

writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("YOUR-PASSWORD-HERE")

-

saving the New PDF

Copy and update the pdf_encryption.py file:


# pdf_encryption.py

from PyPDF2 import PdfReader, PdfWriter
reader = PdfReader("WBW3.pdf")

writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("YOUR-PASSWORD-HERE")

# add this
with open("blockchain.pdf", "wb") as f:
    writer.write(f)

```
---
15. ***Rotate PDF***
```
 import PyPDF2

    pdf_in = open('original.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        if pagenum % 2:
            page.rotateClockwise(180)
        pdf_writer.addPage(page)

    pdf_out = open('rotated.pdf', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
```
---

