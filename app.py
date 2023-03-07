import os
from dotenv import load_dotenv
import telebot
from letters import letters

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN", default= None)

bot = telebot.TeleBot(BOT_TOKEN)


def welcome_func(message:telebot.types.Message):
    bot.reply_to(message, 'Welcome')

def transliter(message:telebot.types.Message):
    he_result = ""
    ar_result = ""
    message_text = message.text.lower()
    for letter in message_text:
        if letter in list(letters.keys()):
            he_result += letters[letter][0]
            ar_result += letters[letter][1]
        else:
            he_result += letter
            ar_result += letter
    he_result = he_result.replace("s²", "שׁ").replace("s¹", "ס").replace("s³", "ס")
    ar_result = ar_result.replace("s²", "ش").replace("s¹", "س").replace("s³", "س")
    bot.reply_to(
        message=message, 
        text=he_result)
    bot.reply_to(
        message=message, 
        text=ar_result)


bot.register_message_handler(commands=['start', 'help'], callback=welcome_func)
bot.register_message_handler(func=lambda x:x, callback=transliter)
if __name__ == "__main__":
    bot.infinity_polling()