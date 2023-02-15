import telebot
import datetime
import threading
import random

BOT_TOKEN = '5725350819:AAFya5pw6KGoce8koCzkSQdsi7EGFAkknt4'
bot = telebot.TeleBot(BOT_TOKEN)
mensajes_aleatorios = ["Y como vienen con las tareas chicos?", "Hola chicos, quería saber si tienen alguna duda", "Chicos, cómo venimos con los pendientes?", "Chicos, me pregunta Lord PM para cuando salimos a prod"]

hora_inicio = datetime.time(10, 0, 0)
hora_fin = datetime.time(17, 0, 0)

@bot.message_handler(commands=['start'])
def enviar_mensaje_de_bienvenida(message):
    bot.reply_to(message, "¡Hola! Soy un bot de Telegram")

@bot.message_handler(commands=['dogger'])
def iniciar_temporizador(message):
    t = threading.Thread(target=enviar_mensaje_programado)
    t.start()
    bot.send_message(chat_id=message.chat.id, text="Recibirás un mensaje del dog cada 2 a 3 horas dentro del rango horario permitido (10 AM a 5 PM).")

def enviar_mensaje_programado():
    while True:
        hora_actual = datetime.datetime.now().time()
        if hora_inicio <= hora_actual <= hora_fin:
            tiempo_espera = random.randint(7200, 10800)
            mensaje = random.choice(mensajes_aleatorios)
            bot.send_message(chat_id, mensaje)
            time.sleep(tiempo_espera)
        else:
            time.sleep(3600)

# Inicia el bot
bot.polling()
