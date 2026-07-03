import os
import random
import requests
import praw

reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"],
    user_agent="Discord Meme Bot"
)

subs = [
    "memes",
    "dankmemes",
    "shitposting",
    "funny"
]

subreddit = reddit.subreddit(random.choice(subs))

posts = []

for post in subreddit.hot(limit=50):
    if (
        not post.stickied
        and not post.over_18
        and post.url.endswith((".jpg",".png",".jpeg",".gif"))
    ):
        posts.append(post)

meme = random.choice(posts)

requests.post(
    os.environ["WEBHOOK"],
    json={
        "content": f"😂 **{meme.title}**\n{meme.url}"
    }
)
