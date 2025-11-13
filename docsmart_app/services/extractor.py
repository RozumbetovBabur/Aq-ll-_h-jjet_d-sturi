# simple PDF extractor using PyPDF2
from PyPDF2 import PdfReader




def extract_text_from_pdf(file_obj):
    """file_obj can be InMemoryUploadedFile or a path-like object"""
    try:
        reader = PdfReader(file_obj)
        pages = []
        for p in reader.pages:
            text = p.extract_text() or ''
            pages.append(text)
            return '\n'.join(pages)
    except Exception:
        # Fallback: try reading file as text
        try:
            file_obj.seek(0)
            return file_obj.read().decode('utf-8', errors='ignore')
        except Exception:
            return ''