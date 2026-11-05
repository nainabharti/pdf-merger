from pypdf import PdfReader , PdfWriter

# Read the first PDF file
pdf1 = PdfReader("test_files/file1.pdf")

# Read the second PDF file
pdf2 = PdfReader("test_files/file2.pdf")

#Count the total pages in each PDF
print("File 1 total pages: ",
      len(pdf1.pages))
print("File 2 total pages: ",
      len(pdf2.pages))

# Create a PDF writer object
writer = PdfWriter()

#Add Pages from the first PDF
for page in pdf1.pages:
    writer.add_page(page)

#Add Pages from the second PDF
for page in pdf2.pages:
    writer.add_page(page)

#Save the merged PDF
with open("output/merged.pdf", "wb") as output_file:
    writer.write(output_file)

print("PDFs merged successfully!")
print("Merged PDF saved in output/merged.pdf") 