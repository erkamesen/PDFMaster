from pypdf import PdfMerger
import time

pdfs = ['1.pdf', '2.pdf', "3.pdf", "4.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

a = time.time()
merger.write("result.pdf")
merger.close()
b = time.time()

print(b-a)
