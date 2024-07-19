
# from dotenv import load_dotenv
import telebot
import time
import json
fs = open('secret.json')
tken = json.load(fs)


# load_dotenv()
# TOKN = os.getenv('TOKEN')
bot = telebot.TeleBot(tken["Secrets"]["TOKEN"], parse_mode=None)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message.chat.id, """how r u a!\
                \n114514""")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message.chat.id, message.text)
    print("message replyed")
@bot.message_handler(commands=['time'])
def send_time_now(message):
    currect_time_str = time.localtime()
    bot.reply_to(message.chat.id, f"{currect_time_str}")

bot.infinity_polling()