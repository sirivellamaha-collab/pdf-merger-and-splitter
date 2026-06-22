from pypdf import PdfReader, PdfWriter, PdfMerger

# Merge multiple PDF files into a single PDF
def merge_pdfs(files, output_file):
    merger = PdfMerger()

    # Add all selected PDF files
    for f in files:
        merger.append(f)

    # Save the merged PDF
    merger.write(output_file)
    merger.close()

# Split a PDF into individual pages
def split_pdf(pdf_file, output_folder):
    reader = PdfReader(pdf_file)

    # Create a separate PDF for each page
    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)

        # Save each page as a new PDF file
        with open(f"{output_folder}/page_{i}.pdf", "wb") as fp:
            writer.write(fp)

# Extract selected pages from a PDF
def extract_pages(pdf_file, pages, output_file):
    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    # Add only the pages selected by the user
    for p in pages:
        writer.add_page(reader.pages[p - 1])

    # Save extracted pages to a new PDF
    with open(output_file, "wb") as fp:
        writer.write(fp)

# Get basic information about a PDF file
def pdf_info(pdf_file):
    reader = PdfReader(pdf_file)

    # Return page count and metadata
    return {
        'pages': len(reader.pages),
        'metadata': str(reader.metadata)
    }