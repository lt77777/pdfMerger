import os
import sys
import pyPDF2

merger = pyPDF2.PdfFileMerger()

for f in os.listdir(os.curdir):
    if f.endswith(".pdf"):
        merger.append(f)
    merger.write("combined.pdf")
