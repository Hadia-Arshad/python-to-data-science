from PyPDF2 import PdfWriter
import os
# path to the folder containg the pdfs
pdf_folder = "merge pdf (2)"
merger = PdfWriter()
files = [file for file in os.listdir(pdf_folder) if file.endswith(".pdf")]
files.sort() # optional for consistent order
for pdf in files:
    filepath = os.path.join(pdf_folder, pdf)
    merger.append(filepath)
merger.write("merged-pdf.pdf")
merger.close()