import telebot
import os

BOT_TOKEN = os.getenv("6727394719:AAFmDh44DO1V-EmXSC9k7r7waiWadJsWI3k")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Bot ishlayapti ✅")

bot.polling()
