PDF Merger

A simple Python-based PDF Merger that allows users to combine multiple PDF files into a single PDF document. It provides features such as custom output filenames, duplicate file detection, error handling, and support for password-protected PDFs.

Features

- Merge Multiple PDFs: Combine multiple PDF files into one document.
- Custom File Paths: Enter PDF file paths manually.
- Custom Output Filename: Choose the name of the merged PDF.
- File Validation: Check whether the provided file paths exist.
- Error Handling: Handle errors while reading and processing PDF files.
- Duplicate Detection: Prevent the same file path from being merged more than once.
- Encrypted PDF Support: Enter a password to process password-protected PDFs.
- Overwrite Protection: Ask for confirmation before overwriting an existing output file.
- Page Count: Display the total number of pages in the merged PDF.
- Merge Summary: Display successfully processed files, skipped files, reasons for skipping, and the total page count.

Technologies Used

- Python – Core programming language.
- pypdf – Python library for reading, modifying, and merging PDF files.
- os module – Used for file path handling and directory management.

Project Structure

pdf-merger/
│
├── output/
│   └── .gitkeep
│
├── test_files/
│   ├── file1.pdf
│   └── file2.pdf
│
├── pdf_merger.py
├── requirements.txt
├── .gitignore
└── README.md

«Note: The ".venv" virtual environment is not included in the repository.»

Installation and Setup

1. Clone the Repository

git clone https://github.com/nainabharti/pdf-merger.git

2. Navigate to the Project Folder

cd pdf-merger

3. Create a Virtual Environment

python -m venv .venv

4. Activate the Virtual Environment

For Windows PowerShell:

.venv\Scripts\Activate.ps1

5. Install Dependencies

pip install -r requirements.txt

How to Run

Run the following command:

python pdf_merger.py

Example

Step 1: Enter PDF file paths separated by commas.

Enter PDF file paths separated by commas:
test_files/file1.pdf, test_files/file2.pdf

Step 2: Enter the desired output filename.

Enter output filename: college.pdf

Step 3: The program processes the PDF files and saves the merged document inside the "output" folder.

PDFs merged successfully!
Merged PDF saved in output/college.pdf

Output

The merged PDF is saved in the "output/" directory.

output/
└── college.pdf

Concepts Learned

Through this project, I practised:

- File handling in Python.
- Working with external Python libraries.
- Functions and modular programming.
- Lists and sets.
- Conditional statements and loops.
- Exception handling using "try-except".
- Working with file paths using the "os" module.
- Reading and writing PDF files.
- Handling password-protected PDFs.
- Input validation and duplicate detection.

Future Scope

The following improvements can be implemented in future versions:

1. Validate PDF extensions and actual file types.
2. Improve overwrite confirmation by accepting only valid "y/n" responses.
3. Improve the final summary to distinguish successful PDF processing from successful output saving.
4. Add progress messages while merging multiple files.
5. Improve error messages and handle additional edge cases.
6. Add a graphical user interface (GUI).
7. Allow users to select PDF files using a file picker.

Author

Naina Bharti

- GitHub: "@nainabharti" (https://github.com/nainabharti)

---

If you find this project useful, feel free to explore the repository!