#import PyPDF2 for processing
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import os

def SplitPage(path, start, end, outputname):
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
    with open("{}.pdf".format(outputname), "wb") as out:
        pdfwriter.write(out)

    # close pdffilereader object
    f.close()

if __name__ == "__main__":
    start = int(input("start page number:"))
    end = int(input("end page number:"))
    outputname = input("outputname:")
    path = "tarted path"
    SplitPage(path, start, end)
