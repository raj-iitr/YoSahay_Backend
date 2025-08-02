from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.detector import detect_lang


app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/whatsapp-webhook")
async def whatsapp_webhook(request: Request):
    try:
        payload = await request.json()
        message = payload.get("messages", [{}])[0]

        user_phone = message.get("from", "unknown")
        user_text = message.get("text", {}).get("body", "").strip()
        lang = detect_lang(user_text)

        if not user_text:
            raise HTTPException(status_code=400, detail="Missing message text")

        print(f"✅ Simulated Incoming Message")
        print(f"📱 Phone: {user_phone}")
        print(f"📝 Text: {user_text}")
        print(f"🌐 Detected Language: {lang}")

        return JSONResponse(content={"phone": user_phone, "message": user_text, "lang": lang},media_type="application/json; charset=utf-8")
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
