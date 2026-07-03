import os
import requests

webhook = os.environ["WEBHOOK"]

meme = requests.get("https://meme-api.com/gimme").json()

requests.post(
    webhook,
    json={
        "content": f"**{meme['title']}**\n{meme['url']}"
    }
)
