import re

def execute_sliding_window_chunking(subtitle_raw_stream: str, window_size_tokens: int = 40, overlap_tokens: int = 15) -> list:
    """Transforms raw stream strings into overlapping text buffers to preserve narrative context layers."""
    # Split out words tokens array
    words = subtitle_raw_stream.split()
    chunks_collection = []
    
    index = 0
    while index < len(words):
        # Extract sliding boundary slices
        window_slice = words[index : index + window_size_tokens]
        chunk_string = " ".join(window_slice)
        chunks_collection.append(chunk_string)
        
        # Advance index by step size (window_size - overlap)
        index += (window_size_tokens - overlap_tokens)
        
    return chunks_collection

def strip_subtitle_timestamp_noise(raw_srt_content: str) -> str:
    """Uses optimized Regular Expression pattern filters to clean timeline layout overhead."""
    # Expression matching subtitle indices numbers sequence block
    clean_pass_1 = re.sub(r'^\d+\s*$', '', raw_srt_content, flags=re.MULTILINE)
    
    # Expression matching time window telemetry structures (e.g., 00:01:20,000 --> 00:01:23,120)
    clean_pass_2 = re.sub(r'\d{2}:\d{2}:\d{2}[,.]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[,.]\d{3}', '', clean_pass_1)
    
    # Compress empty structural white space loops
    return " ".join(clean_pass_2.split())
