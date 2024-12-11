import telebot
from telebot import types
from settings import token
import requests
from bs4 import BeautifulSoup

print("Version: 1.1 - 11.12.24\n"
      "Start 🗽⃢⃢🗿")

header = {
    'user-agent': 'Slinux'
}

factlink = 'https://randstuff.ru/fact/'
filmlink = 'https://randomfilm.ru'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["fact"])
def factin(message):
    response = requests.get(factlink, headers=header).text
    soup = BeautifulSoup(response, 'lxml')
    fact = soup.find('div', id="fact").text

    facts = fact.replace("ПресноИнтересно", "")
    bot.send_message(message.chat.id, "<b>🎲 Случайный факт:</b>\n"
                                      "\n"
                                      f"{facts}", parse_mode='html')

@bot.message_handler(commands=["film"])
def filmin(message):
    response2 = requests.get(filmlink, headers=header).text
    soup2 = BeautifulSoup(response2, 'lxml')
    block3 = soup2.find('div', align="center", style="width: 100%").text
    block4 = soup2.find('div', align="center", style="width: 100%").img['src']

    main = block3.replace("ТРЕЙЛЕРСМОТРЕТЬ ФИЛЬМ", "")
    bot.send_message(message.chat.id, "<b>🎲 Случайный фильм:</b>\n"
                                      f"{main}\n\n"
                                      f"{"https://randomfilm.ru/" + block4}", parse_mode='html')

@bot.message_handler(commands=["start"])
def beginning(message):
    bot.send_message(message.chat.id, "🔍 Добро пожаловать в telegram-бот Фактоид")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    block1 = types.KeyboardButton("📝 Факт")
    block2 = types.KeyboardButton("🎥 Фильм")

    #markup.add(block1)
    markup.row(block1)
    markup.row(block2)
    bot.send_message(message.chat.id,"Мы можете сгенерировать случаный:\n\n"
                                     "1. Факт\n"
                                     "2. Фильм\n\n"
                                     "Нажмите на желаемую кнопку".format(message.from_user),reply_markup=markup)

@bot.message_handler(content_types=["text"])
def log(message):
    if message.chat.type == 'private' and message.text == '📝 Факт':
        response = requests.get(factlink, headers=header).text
        soup = BeautifulSoup(response, 'lxml')
        fact = soup.find('div', id="fact").text

        facts = fact.replace("ПресноИнтересно", "")
        bot.send_message(message.chat.id, "<b>🎲 Случайный факт:</b>\n"
                                            "\n"
                                            f"{facts}", parse_mode='html')

    elif message.chat.type == 'private' and message.text == '🎥 Фильм':
        response2 = requests.get(filmlink, headers=header).text
        soup2 = BeautifulSoup(response2, 'lxml')
        block3 = soup2.find('div', align="center", style="width: 100%").text
        block4 = soup2.find('div', align="center", style="width: 100%").img['src']

        main = block3.replace("ТРЕЙЛЕРСМОТРЕТЬ ФИЛЬМ", "")
        bot.send_message(message.chat.id, "<b>🎲 Случайный фильм:</b>\n"
                                          f"{main}\n\n"
                                          f"{"https://randomfilm.ru/" + block4}", parse_mode='html')

bot.polling(none_stop=True)