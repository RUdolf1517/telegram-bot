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

@bot.message_handler(commands=['joke', 'шутку'])
def send_joke(message):
    # Открываем файл с шутками
    with open('jokes.txt', 'r', encoding='utf-8') as file:
        jokes = file.readlines()

    # Выбираем случайную шутку
    joke = random.choice(jokes)

    # Отправляем шутку пользователю
    bot.reply_to(message, joke)

print("start")
bot.polling()
