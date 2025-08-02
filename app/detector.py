# This code is part of a FastAPI application that detects the language of a given text.
# It uses the langdetect library to identify the language and returns a string representation.

from langdetect import detect

# Function to detect the language of a given text
# It returns "hi" for Hindi, "en" for English, and "hi-en
def detect_lang(text: str) -> str:
    try:
        lang = detect(text)
        if lang == "hi":
            return "hi"
        elif lang == "en":
            return "en"
        else:
            return "hi-en"  # assume Hinglish or code-mix
    except:
        return "unknown"
