#import PyPDF2 for processing
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import os

def SplitPage(path, start, end):
    #create file object for target pdf
    f = open(path, "rb")

    #create PdfFileReader object from file object
    pdf = PdfFileReader(f)

    #create a pdfwriter object
    pdfwriter = PdfFileWriter()


    for pagenb in range(start-1, end):
        #add page to pdfwriter object
        pdfwriter.addPage(pdf.getPage(pagenb))


    #open a new file and write pdf to it
    with open("Ch54.pdf", "wb") as out:
        pdfwriter.write(out)

    # close pdffilereader object
    f.close()

if __name__ == "__main__":
    start = int(input("start page number:"))
    end = int(input("end page number:"))
    path = "C:\\Users\\B85M-ADATA480G\\Desktop\\pdf editing software\\Fitz.pdf"
    SplitPage(path, start, end)