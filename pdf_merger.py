import os
from pypdf import PdfReader, PdfWriter

# Take PDF file paths from the user
pdf_files = input("Enter PDF file paths separated by commas: ")

# Convert input into a list
pdf_files = pdf_files.split(",")

# Create a PDF writer object
writer = PdfWriter()

# Read and merge all selected PDF files
for file in pdf_files:
    file = file.strip()

    # Check whether the file exists
    if os.path.exists(file):

        try:
            # Read the PDF file
            pdf = PdfReader(file)

            print(file, "total pages:", len(pdf.pages))

            # Add pages to the writer
            for page in pdf.pages:
                writer.add_page(page)

        except Exception as error:
            print("Could not process", file, ":", error)

    else:
        print("File not found:", file)

# Check whether any pages were added
if len(writer.pages) > 0:

    # Save the merged PDF
    with open("output/merged.pdf", "wb") as output_file:
        writer.write(output_file)

    print("PDFs merged successfully!")
    print("Merged PDF saved in output/merged.pdf")

else:
    print("No valid PDF pages found. Nothing to merge.")