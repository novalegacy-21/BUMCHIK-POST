import telebot

BOT_TOKEN = "7694488473:AAFa_MqdHABWpb1BYdgUUCEJcVkJQyi5hjU"
bot = telebot.TeleBot(BOT_TOKEN)

DEFAULT_IMAGE = 'https://i.postimg.cc/GpZcyLwr/Adobe-Express-file.png'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "✅ Bot is active! Send me a link.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if "http" in message.text:
        bot.send_photo(
            message.chat.id,
            DEFAULT_IMAGE,
            caption=f"🔗 {message.text}",
            parse_mode="HTML"
        )
    else:
        bot.send_message(message.chat.id, message.text)

bot.infinity_polling()