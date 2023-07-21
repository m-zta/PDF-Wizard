import os
import sys
import PyPDF2

"""
Extracts the text from all the PDFs in the input directory and saves
it to a single output file.
"""


def extract_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def transfer_text(input_dir, output_file):
    with open(output_file, 'w') as output:
        for filename in os.listdir(input_dir):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(input_dir, filename)
                text = extract_from_pdf(pdf_path)
                output.write(text)

    # Print success message
    print(f"Text extracted from PDFs and saved to {output_file}.")


def main():
    # Check if the input directory exists
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_text.py <directory_path>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_file = "output.txt"

    # Check if the input directory exists
    if not os.path.isdir(input_dir):
        print("Invalid directory path.")
        sys.exit(1)

    transfer_text(input_dir, output_file)

    print(f"Text extracted from PDFs and saved to {output_file}.")


if __name__ == "__main__":
    main()
