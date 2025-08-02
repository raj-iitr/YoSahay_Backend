import requests
import json

payload = {
    "messages": [{
        "from": "919876543210",
        "text": {
            "body": "मुझे प्रधानमंत्री किसान योजना की जानकारी चाहिए।"
        },
        "type": "text"
    }]
}

res = requests.post("http://localhost:8000/whatsapp-webhook", json=payload)
print(res.json())
