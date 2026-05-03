import os
import requests
from bs4 import BeautifulSoup
import telegram

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@freelance_free_11"

bot = telegram.Bot(token=TOKEN)

def parse_kwork():
    url = "https://kwork.ru/projects"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    projects = soup.find_all("a", class_="wants-card__title")[:5]

    results = []
    for project in projects:
        title = project.text.strip()
        link = "https://kwork.ru" + project["href"]
        results.append(f"🔥 {title}\n{link}")

    return results

def main():
    projects = parse_kwork()
    for project in projects:
        bot.send_message(chat_id=CHANNEL, text=project)

if __name__ == "__main__":
    main()
