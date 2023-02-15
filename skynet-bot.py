import telebot
import random

# Inserta aquí el token de tu bot
BOT_TOKEN = '5725350819:AAFya5pw6KGoce8koCzkSQdsi7EGFAkknt4'

bot = telebot.TeleBot(BOT_TOKEN)

messages = ["Qué te pasa pelotudo?", "Qué agita gil?", "Bueno loco, mira que le digo al dog", "Pasame tu dni", "Saludos cordiales"]

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    response = random.choice(messages)
    bot.reply_to(message, response)

bot.infinity_polling()
