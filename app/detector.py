from langdetect import detect

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
