import os
import requests
import telegram
import xml.etree.ElementTree as ET

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@freelance_free_11"

bot = telegram.Bot(token=TOKEN)

RSS_URL = "https://freelance.habr.com/tasks.rss"

def parse_rss():
    response = requests.get(RSS_URL)
    root = ET.fromstring(response.content)

    items = []
    for item in root.findall(".//item")[:5]:
        title = item.find("title").text
        link = item.find("link").text
        items.append(f"🔥 {title}\n{link}")

    return items

def main():
    posts = parse_rss()
    for post in posts:
        bot.send_message(chat_id=CHANNEL, text=post)

if __name__ == "__main__":
    main()
