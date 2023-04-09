from pypdf import PdfMerger
import time
import os


class PDFMaster:
    def __init__(self):
        os.chdir("/home/erkam/Files/PDFMaster/static/files")
        self.current_time = str(round(time.time()))
        os.mkdir(self.current_time)
        os.chdir(self.current_time)

    def merge_pdf(self, filenames):
        
        merger = PdfMerger()
        for filename in filenames:
            try:
                merger.append(f"{filename}")
            except:
                continue
        
        
        merger.write("result.pdf")
        merger.close()
        return self.current_time

if __name__ == "__main__":
    _merger = PDFMaster()
    _merger.merge_pdf(filenames=["1.pdf", "2.pdf"])




