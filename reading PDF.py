import pdfplumber

def extract_text_from_pdf(pdf_file_path):
    try:
        with pdfplumber.open(pdf_file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error occurred while parsing PDF: {e}")
        return None
pdf_file_path = "C:/Users/DELL/Documents/Survey Response.pdf"
response_text = extract_text_from_pdf(pdf_file_path)
if response_text:
    print(response_text)