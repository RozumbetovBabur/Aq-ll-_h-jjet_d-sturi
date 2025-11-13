# Simple naive summarizer: takes first N sentences. Replace with HF pipeline for better results.

import re

def summarize_text(text, max_sentences=3):
    if not text:
        return ''
    # split into sentences (very naive)
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return ' '.join(sentences[:max_sentences])