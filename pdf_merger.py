import os
from pypdf import PdfReader, PdfWriter


# 1. Function to get PDF file paths
def get_pdf_files():

    pdf_files = input("Enter PDF file paths separated by commas: ")

    # Convert input into a list
    pdf_files = pdf_files.split(",")

    return pdf_files


# 2. Function to get output filename
def get_output_path():

    output_name = input("Enter output filename: ")

    # Remove extra spaces
    output_name = output_name.strip()

    # Add .pdf extension if not present
    if not output_name.lower().endswith(".pdf"):
        output_name += ".pdf"

    # Create output path
    output_path = os.path.join("output", output_name)

    # Check if the output file already exists
    if os.path.exists(output_path):
        choice = input("File already exists, Overwrite? (y/n): ")
        choice = choice.strip().lower()

        if choice == "y":
            return output_path
        else:
            return None

    return output_path


# 3. Function to merge PDF files
def merge_pdfs(pdf_files, output_path):

    # Create a PDF writer object
    writer = PdfWriter()

    # Process each PDF file
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

        try:
            # Create output folder if it doesn't exist
            os.makedirs("output", exist_ok=True)

            # Save the merged PDF
            with open(output_path, "wb") as output_file:
                writer.write(output_file)

            print("\nPDFs merged successfully!")
            print("Merged PDF saved in", output_path)

        except Exception as error:
            print("Could not save the merged PDF:", error)

    else:
        print("\nNo valid PDF pages found. Nothing to merge.")


# 4. Main function
def main():

    # Get PDF file paths
    pdf_files = get_pdf_files()

    # Get output filename
    output_path = get_output_path()

    # Merge PDF files
    if output_path is not None:
        merge_pdfs(pdf_files, output_path)
    else:
        print("PDF merging cancelled.")


# Main program execution
if __name__ == "__main__":
    main()