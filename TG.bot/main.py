import telebot #Библиотека
from BOT import * #Импортируем токена
from time import sleep #отвечает на несколько секунд


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, 'Здарова чо нада')
    elif message.text == "Как дела":
        sleep(2)
        bot.send_message(message.from_user.id, 'отлично ')
    elif message.text == "Что делаешь":
        sleep(2)
        bot.send_message(message.from_user.id, 'конечно обшаюсь')
    elif message.text == "/start":
        bot.send_message(message.from_user.id, 'добро пожаловать на мой телеграмм бот!')
    elif message.text == "Как тебя зовут":
        bot.send_message(message.from_user.id, 'Меня зовут AYLCHY а тебя как?')
    elif message.text == "Байэл":
        bot.send_message(message.from_user.id, 'Приятно познакомится, Баэл ')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понял')
#Запуск бота на бесконечный опрос новых сообщений:
bot.infinity_polling()