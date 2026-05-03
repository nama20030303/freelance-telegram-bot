import os
import telegram
import feedparser

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@freelance_free_11"

bot = telegram.Bot(token=TOKEN)

RSS_URL = "https://freelance.habr.com/tasks.rss"

def parse_rss():
    feed = feedparser.parse(RSS_URL)
    posts = []

    for entry in feed.entries[:5]:
        title = entry.title
        link = entry.link
        posts.append(f"🔥 {title}\n{link}")

    return posts

def main():
    posts = parse_rss()

    if not posts:
        bot.send_message(chat_id=CHANNEL, text="⚠️ RSS временно недоступен")
        return

    for post in posts:
        bot.send_message(chat_id=CHANNEL, text=post)

if __name__ == "__main__":
    main()
