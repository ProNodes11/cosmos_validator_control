import subprocess
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import json
# Конфигурация
API_URL = "https://validators.cosmos.directory/chains/"
user_info = "1368677439"
with open("validator_list.txt", "r") as f:
    dat = f.read()
with open("command_list.txt", "r") as f:
    comman = f.read()
datas = json.loads(dat)
commands = json.loads(comman)
TELEGRAM_BOT_TOKEN = "7439796246:AAHcE_uuLO6XlGf5LHXbLlLSyZlyx3gNM7U"
def scheduled_task(context: CallbackContext):
    for i in range(len(datas)):
        print(datas[i])
        try:
            data = requests.get(datas[i]).json()
            name = data['name']
            print(data['validator']['active'])
            if data['validator']['active']==True:
                suzik = "🟢🟢🟢|"
            else:
                suzik = "🔴🔴🔴|"
                context.bot.send_message(chat_id=chat_id, text=f"{name} - {suzik}")
    
        except Exception as e:
            update.message.reply_text(f"An error occurred: {e}")
def main():
    """Запуск бота."""
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    
    dp = updater.dispatcher
    job = updater.job_queue
    job.run_repeating(scheduled_task, interval=60, first=0)
    # Запускаем бота
    updater.start_polling()
    
    # Ждем завершения работы
    updater.idle()

if __name__ == "__main__":
    main()
