import os
import random
import requests

webhook = os.environ["WEBHOOK"]

meme = requests.get("https://meme-api.com/gimme").json()

mensajes = [
    "🏍️ Un motociclista dejó esto por aquí...",
    "🍺 Ya llegó el meme rancio del rato.",
    "☠️ La Iron Legion aprueba este meme.",
    "🔥 Encontrado en Reddit.",
    "🛠️ El mecánico encontró esta joyita.",
    "😂 Meme recién robado de Reddit.",
    "⚙️ El taller encontró esta obra de arte.",
    "🏍️ El camino estuvo largo, pero valió la pena."
]

mensaje = random.choice(mensajes)

requests.post(
    webhook,
    json={
        "content": f"{mensaje}\n\n**{meme['title']}**\n{meme['url']}"
    }
)
