from pypdf import PdfReader

# Read the first PDF file
pdf1 = PdfReader("test_files/file1.pdf")

# Read the second PDF file
pdf2 = PdfReader("test_files/file2.pdf")

#Count the total pages in each PDF
print("File 1 total pages: ",
      len(pdf1.pages))
print("File 2 total pages: ",
      len(pdf2.pages))
