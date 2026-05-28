from pypdf import PdfReader
import io

def convert_pdf_to_clean_tokens(file_buffer: io.BytesIO) -> str:
    """Ingests high-density unstructured text layers out of standard PDF binaries."""
    try:
        reader = PdfReader(file_buffer)
        extracted_text = ""
        for page in reader.pages:
            text_layer = page.extract_text()
            if text_layer:
                extracted_text += text_layer + "\n"
        
        # Simple cleanup formatting normalization
        normalized_tokens = " ".join(extracted_text.split())
        return normalized_tokens
    except Exception as e:
        raise RuntimeError(f"Failed to cleanly process stream tokens: {str(e)}")
