import os
from pypdf import PdfReader, PdfWriter


def get_pdf_files():
    pdf_files = input("Enter PDF file paths separated by commas: ")
    pdf_files = pdf_files.strip()

    if not pdf_files:
        print("PDF file paths cannot be empty.")
        return None

    pdf_files = pdf_files.split(",")
    return pdf_files


def get_output_path():
    output_name = input("Enter output filename: ")
    output_name = output_name.strip()

    if not output_name:
        print("Filename cannot be empty.")
        return None

    if not output_name.lower().endswith(".pdf"):
        output_name += ".pdf"

    output_path = os.path.join("output", output_name)

    if os.path.exists(output_path):
        choice = input("File already exists. Overwrite? (y/n): ")
        choice = choice.strip().lower()

        if choice == "y":
            return output_path
        else:
            return None

    return output_path


def remove_duplicates(pdf_files):
    unique_files = []
    seen_files = set()

    for file in pdf_files:
        file = file.strip()

        if file not in seen_files:
            unique_files.append(file)
            seen_files.add(file)
        else:
            print("Duplicate file skipped:", file)

    return unique_files


def merge_pdfs(pdf_files, output_path):
    writer = PdfWriter()

    successful_files = []
    skipped_files = []

    for file in pdf_files:
        file = file.strip()

        if os.path.exists(file):
            try:
                pdf = PdfReader(file)

                # Check whether the PDF is encrypted
                if pdf.is_encrypted:
                    password = input(f"Enter password for {file}: ")
                    result = pdf.decrypt(password)

                    if not result:
                        print("Incorrect password. Skipping:", file)
                        skipped_files.append(
                            (file, "Incorrect password")
                        )
                        continue

                print(file, "total pages:", len(pdf.pages))

                for page in pdf.pages:
                    writer.add_page(page)

                successful_files.append(file)

            except Exception as error:
                print("Could not process", file, ":", error)
                skipped_files.append((file, str(error)))

        else:
            print("File not found:", file)
            skipped_files.append((file, "File not found"))

    # Save the merged PDF
    if len(writer.pages) > 0:
        try:
            os.makedirs("output", exist_ok=True)

            with open(output_path, "wb") as output_file:
                writer.write(output_file)

            print("\nPDFs merged successfully!")
            print("Merged PDF saved in", output_path)

        except Exception as error:
            print("Could not save the merged PDF:", error)

    else:
        print("\nNo valid PDF pages found. Nothing to merge.")

    # Display final summary
    print("\n========== MERGE SUMMARY ==========")

    print("Successfully processed files:", len(successful_files))
    print("Skipped files:", len(skipped_files))
    print("Total pages merged:", len(writer.pages))

    if successful_files:
        print("\nSuccessfully processed files:")

        for file in successful_files:
            print("-", file)

    if skipped_files:
        print("\nSkipped files:")

        for file, reason in skipped_files:
            print("-", file, ":", reason)


def main():
    pdf_files = get_pdf_files()

    if pdf_files is None:
        print("PDF merging cancelled.")
        return

    pdf_files = remove_duplicates(pdf_files)

    output_path = get_output_path()

    if output_path is not None:
        merge_pdfs(pdf_files, output_path)
    else:
        print("PDF merging cancelled.")


if __name__ == "__main__":
    main()