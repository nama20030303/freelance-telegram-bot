import os
import telegram

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@freelance_free_11"

bot = telegram.Bot(token=TOKEN)

def main():
    bot.send_message(chat_id=CHANNEL, text="✅ Бот работает! Автопостинг запущен.")

if __name__ == "__main__":
    main()
