import telebot
import random

bot = telebot.TeleBot("6926925203:AAGilRh7PlJK9oFUZjcq8NcvlK1mMLznVkA")

with open('jokes.txt', 'r+') as file:
    lines = file.readlines()
    file.seek(0)  # Перемещаем указатель в начало файла

    for i, line in enumerate(lines, 1):
        if line.startswith(f"{i}:"):
            line = line.split(":", 1)[1]  # Удаляем текущую нумерацию
        file.write(f"{i}: {line}")

    file.truncate()

@bot.message_handler(commands=['помощь', 'help'])
def send_help(message):
    bot.reply_to(message, 'Вот мои команды: \n 1) /help - выводиться необходимая помощь специально для вас \n 2) /joke - выводиться одна из многочисленных шуток')

@bot.message_handler(commands=['start'])
def send_subscribe(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} ! Это чат бот с многочисленными шутками, которые собираются каждый день! Что бы поддержать автора достаточно всего лишь подписаться на его Telegram канал. ССылка тут:")

@bot.message_handler(commands=['joke', 'шутку'])
def send_joke(message):
    # Открываем файл с шутками
    with open('jokes.txt', 'r', encoding='utf-8') as file:
        jokes = file.readlines()

    # Выбираем случайную шутку
    joke = random.choice(jokes)

    # Отправляем шутку пользователю
    bot.reply_to(message, joke)

print("starting...")
bot.infinity_polling(allowed_updates=None)
