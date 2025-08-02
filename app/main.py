#This code is part of a FastAPI application that handles incoming WhatsApp messages.
# It detects the language of the message and returns the phone number, message text, and detected language.

# Necessary imports
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.detector import detect_lang
from dotenv import load_dotenv



app = FastAPI()

load_dotenv()

#Created a health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

#Created a webhook endpoint to handle incoming WhatsApp messages
# It extracts the phone number and message text, detects the language, and returns the information.
@app.post("/whatsapp-webhook")
async def whatsapp_webhook(request: Request):
    body = await request.json()
    message_data = body.get("messages", [{}])[0]

    user_phone = message_data.get("from")
    user_text = message_data.get("text", {}).get("body", "").strip()

    print(f"📱 Phone: {user_phone}")
    print(f"📝 Text: {repr(user_text)}")  # use repr() to debug encoding
    lang = detect_lang(user_text)
    print(f"🌐 Detected Language: {lang}")

    return JSONResponse(content={"phone": user_phone, "message": user_text, "lang": lang})
