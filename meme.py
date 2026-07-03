import os
import random
import requests

WEBHOOK = os.environ["WEBHOOK"]

HEADERS = {
    "User-Agent": "IronLegionDiscordBot/1.0"
}

SUBREDDITS = [
    "MAAU",
    "Mujico",
    "BeelcitosMemes",
    "memes",
    "dankmemes",
    "funny"
]

MENSAJES = [
    "🏍️ Un motociclista dejó esto por aquí...",
    "🍺 Ya llegó el meme rancio del rato.",
    "☠️ La Iron Legion aprueba este meme.",
    "🔥 Encontrado en Reddit.",
    "🛠️ El mecánico encontró esta joyita.",
    "😂 Meme recién robado de Reddit."
]

def obtener_meme():

    random.shuffle(SUBREDDITS)

    for sub in SUBREDDITS:

        url = f"https://www.reddit.com/r/{sub}/hot.json?limit=40"

        try:

            data = requests.get(url, headers=HEADERS, timeout=10).json()

            posts = []

            for p in data["data"]["children"]:

                post = p["data"]

                if post["over_18"]:
                    continue

                if post["stickied"]:
                    continue

                if post["is_video"]:
                    continue

                imagen = post["url"]

                if not imagen.endswith((".jpg",".jpeg",".png",".gif")):
                    continue

                posts.append(post)

            if posts:

                elegido = random.choice(posts)

                return {
                    "titulo": elegido["title"],
                    "imagen": elegido["url"],
                    "subreddit": sub
                }

        except:
            pass

    return None


meme = obtener_meme()

if meme:

    mensaje = random.choice(MENSAJES)

    requests.post(

        WEBHOOK,

        json={

            "content":
f"""{mensaje}

📍 r/{meme['subreddit']}

**{meme['titulo']}**

{meme['imagen']}"""
        }

    )
