import telebot
from telebot import types
import random
import io
import time

bot = telebot.TeleBot("")

print("starting...")

with io.open('jokes.txt', 'r+', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()
    file.seek(0)  # Перемещаем указатель в начало файла

    for i, line in enumerate(lines, 1):
        if line.startswith(f"{i}:"):
            line = line.split(":", 1)[1]  # Удаляем текущую нумерацию
        file.write(f"{i}:{line}")

    file.truncate()

@bot.message_handler(commands=['помощь', 'help'])
def send_help(message):
    bot.reply_to(message, 'Вот мои команды: \n 1) /help - выводиться необходимая помощь специально для вас \n 2) /joke - выводиться одна из многочисленных шуток')

@bot.message_handler(commands=['start'])
def send_subscribe(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}! Это чат бот с многочисленными шутками, которые собираются каждый день! Что бы поддержать автора достаточно всего лишь подписаться на его Telegram канал. ССылка тут: https://t.me/txhtrh")

@bot.message_handler(commands=['amount_of_jokes'])
def send_amount_of_jokes(message):
    with open('jokes.txt', 'r+', encoding='utf-8', errors='ignore') as file:
        line_count = 0
        lines = file.readlines()
        line_count = len(lines)
    bot.reply_to(message, f'кол-во шуток в базе: {line_count}')


@bot.message_handler(commands=['joke', 'шутку'])
def send_joke(message):
    # Открываем файл с шутками
    with open('jokes.txt', 'r+', encoding='utf-8', errors='ignore') as file:
        jokes = file.readlines()

    # Выбираем случайную шутку
    joke = random.choice(jokes)

    # Отправляем шутку пользователю
    bot.reply_to(message, joke)


def send_joke_to_channel():
    with open('jokes.txt', 'r+', encoding='utf-8', errors='ignore') as file:
        jokes = file.read().splitlines()
        joke = random.choice(jokes)
        bot.send_message('-1001997262813', joke)

print("ready")
bot.infinity_polling(allowed_updates=None)

while True:
    current_time = time.strftime("%H:%M", time.gmtime())
    if current_time == "9:30" or current_time == "13:30" or current_time == "20:23":  # Установите желаемое время для отправки шутки
        send_joke_to_channel()
        time.sleep(30)  # Проверка времени


