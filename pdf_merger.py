import os
from pypdf import PdfReader, PdfWriter

# Take PDF file paths from the user
pdf_files = input("Enter PDF file paths separated by commas: ")

# Convert input into a list
pdf_files = pdf_files.split(",")

# Take output filename from the user
output_name = input("Enter output filename: ")

# Remove extra spaces
output_name = output_name.strip()

# Add .pdf extension if not already present
if not output_name.endswith(".pdf"):
    output_name += ".pdf"

# Create output file path
output_path = os.path.join("output", output_name)

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
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print("PDFs merged successfully!")
    print("Merged PDF saved in", output_path)

else:
    print("No valid PDF pages found. Nothing to merge.")