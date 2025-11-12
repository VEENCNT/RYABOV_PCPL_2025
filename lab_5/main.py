import telebot

from telebot import types
from random import randint

russian_quotes = [
    "\"Работа не волк. Никто не волк. Только волк — волк.\"",
    "\"Мама учила не ругаться матом, но жизнь научила не ругаться матом при маме.\"",
    "\"Если тебе где-то не рады в рваных носках, то и в целых туда идти не стоит.\"",
    "\"Тут — это вам не там.\"",
    "\"Кто рано встает — тому весь день спать хочется.\"",
    "\"Все что не делается, я не делаю\"",
    "\"Хожу дома в одних трусах, потому что в двух жарко\"",
    "\"Крепче знаешь, меньше спишь\"",
    "\"Если тебя обидели незаслуженно - вернись и заслужи\"",
    "\"Однажды дважды не бывает\""
]

russian_quotes_amount = len(russian_quotes)

english_quotes = [
    "\"Work is not a wolf. No one is a wolf. Just a wolf, a wolf.\"",
    "\"Mom taught me not to swear, but life has taught me not to swear in front of my mom.\"",
    "\"If you are not welcome in torn socks somewhere, then you should not go there in whole ones.\"",
    "\"Here is not there.\"",
    "\"Anyone who gets up early wants to sleep all day.\"",
    "\"Whatever is not being done, I am not doing.\"",
    "\"I go home in only my underpants because it's hot in two\"",
    "\"Once doesn't happen twice\"",
    "\"If you've been wronged, come back and earn it.\"",
    "\"How old is a man, how many winters does he have\""
]

english_quotes_amount = len(english_quotes)

with open("key.txt") as file:
    key = file.read()

bot = telebot.TeleBot(key)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    russian_button = types.KeyboardButton("🇷🇺 Русский")
    english_button = types.KeyboardButton("🇬🇧 English")
    markup.add(russian_button, english_button)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "🇷🇺 Русский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        generate_quote_button = types.KeyboardButton(text="Сгенерировать цитату")
        markup.add(generate_quote_button)
        bot.send_message(message.from_user.id, "Чем я могу помочь? 🤔", reply_markup=markup)
    elif message.text == "Сгенерировать цитату":
        random_russian_quote = russian_quotes[randint(0, russian_quotes_amount - 1)]
        bot.send_message(message.from_user.id, f"{random_russian_quote} - Джейсон Стетхем (c)", parse_mode='Markdown')
    elif message.text == "🇬🇧 English":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        generate_quote_button = types.KeyboardButton(text="Generate quote")
        markup.add(generate_quote_button)
        bot.send_message(message.from_user.id, "How can i help you? 🤔", reply_markup=markup)
    elif message.text == "Generate quote":
        random_english_quote = english_quotes[randint(0, english_quotes_amount - 1)]
        bot.send_message(message.from_user.id, f"{random_english_quote} - Jason Statham (c)", parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)