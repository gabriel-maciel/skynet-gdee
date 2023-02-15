import telegram

# Inserta aquí el token de tu bot
TOKEN = '5725350819:AAFya5pw6KGoce8koCzkSQdsi7EGFAkknt4'

def hello_world(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World!')

def main():
    # Crea una instancia del bot
    bot = telegram.Bot(token=TOKEN)

    # Crea un despachador para el bot
    dispatcher = telegram.Dispatcher(bot, None, workers=0)

    # Agrega un manejador para el comando /start
    dispatcher.add_handler(telegram.CommandHandler('start', hello_world))

    # Inicia el bot
    bot.start_polling()

if __name__ == '__main__':
    main()
