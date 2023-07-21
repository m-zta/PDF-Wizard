import os
import sys
import PyPDF2
import argparse

"""
Extracts the text from all the PDFs in the input directory and saves
it to a single output file.
"""


def parse_arguments():
    # The 'description' argument gives a brief description of what the program does when the user passes the -h or --help flags.
    parser = argparse.ArgumentParser(
        description='Description: Extracts the text from all the PDFs in the input directory and saves it to a single output file.')
    parser.add_argument('input_dir', type=str,
                        help='The directory containing the PDF files.')
    parser.add_argument('output_file', type=str,
                        help='The file where the extracted text will be saved.')

    # The parse_args() method returns a Namespace object containing the arguments to the command line.
    args = parser.parse_args()

    # Check if the input directory and output file are valid
    if not os.path.isdir(args.input_dir):
        print(f"Invalid directory path: {args.input_dir}")
        sys.exit(1)
    if not os.path.isdir(os.path.dirname(args.output_file)):
        print(f"Invalid directory path: {os.path.dirname(args.output_file)}")
        sys.exit(1)

    return args.input_dir, args.output_file


def extract_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
    except PyPDF2.utils.PdfReadError:
        print(f"Unable to read PDF: {pdf_path}")
        return ""

    # Check if any text was extracted
    if not text:
        print(f"No text found in PDF: {pdf_path}")

    return text


def transfer_text(input_dir, output_file):
    with open(output_file, 'w') as output:
        for filename in os.listdir(input_dir):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(input_dir, filename)
                text = extract_from_pdf(pdf_path)
                if text: # Only write to file if text was extracted
                    output.write(text)

    # Print success message
    print(f"Text extracted from PDFs and saved to {output_file}.")


def main():
    input_dir, output_file = parse_arguments()
    transfer_text(input_dir, output_file)

    print(f"Text extracted from PDFs and saved to {output_file}.")


if __name__ == "__main__":
    main()
