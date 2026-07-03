import os
import requests

WEBHOOK = os.environ["WEBHOOK"]

r = requests.post(
    WEBHOOK,
    json={
        "content":"✅ Prueba exitosa desde GitHub"
    }
)

print(r.status_code)
print(r.text)
