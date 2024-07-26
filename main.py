import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import json
# Конфигурация
API_URL = "https://validators.cosmos.directory/chains/"
with open("validator_list.txt", "r") as f:
    dat = f.read()
datas = json.loads(dat)
TELEGRAM_BOT_TOKEN = ""  # Замените на ваш токен
def len_up(word, leng):
    k=0
    while(len(word)<leng):
        if k==0:
            word = word +" "
            k = k+1
        else:
            word = " " +word
            k = k - 1 
    return word
def validators(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /validators."""
    update.message.reply_text("Запрос обрабатывается, момент!")
    update.message.reply_text(f"`   Chain   | token_amount | usd_value | Status |`\n", parse_mode='Markdown')
    for i in datas:
        try:
            # Получаем данные валидатора
            data = requests.get(i).json()
        
            # Извлекаем нужные данные
            name = len_up(data['name'], 11)
            total_tokens = len_up(str(int(data['validator']['delegations']['total_tokens_display'])), 12)
            commission_rate = len_up(str(int(data['validator']['delegations']['total_usd']))+"$", 10)
            print(data['validator']['active'])
            if data['validator']['active']==True:
                suzik = "🟢🟢🟢|"
            else:
                suzik = "🔴🔴🔴|"
            # Формируем сообщение
            message = (
                f"`{name}| {total_tokens} | {commission_rate}|{suzik}`"
            )        
            # Отправляем сообщение пользователю
            update.message.reply_text(message, parse_mode='Markdown')
    
        except Exception as e:
            update.message.reply_text(f"An error occurred: {e}")

def main():
    """Запуск бота."""
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    
    dp = updater.dispatcher
    
    # Добавляем обработчик команды /validators
    dp.add_handler(CommandHandler("validators", validators))
    
    # Запускаем бота
    updater.start_polling()
    
    # Ждем завершения работы
    updater.idle()

if __name__ == "__main__":
    main()
