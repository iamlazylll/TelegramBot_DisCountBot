
# from dotenv import load_dotenv
import telebot
# from telegram import ParseMode
# from telebot import ParseMode
import time
import json
fs = open('secret.json')
tken = json.load(fs)


# load_dotenv()
# TOKN = os.getenv('TOKEN')
bot = telebot.TeleBot(tken["Secrets"]["TOKEN"], parse_mode=("markdown"))

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """how r u a!\
                \n114514""")

# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)
#     print("message replyed")
@bot.message_handler(commands=['time'])
def send_time_now(message):
    currect_time_str = time.localtime()
    bot.reply_to(message, f"{currect_time_str}")
# def rick_roll_LOL(message, commands=['sing']):
#     lyricss = ""
#     bot.reply_to(message.chat.id, f"{currect_time_str}")
@bot.message_handler(commands=['discount'])
def demo_msg(message):
    text='嗨👋~以下是今天的優惠資訊:\n蝦皮：\n    9.3折[低消2000][商城](https://shopee.tw/)\n    9.5折[低消2000][商城](https://shopee.tw/)'
    bot.reply_to(message, text)
bot.infinity_polling()
# zFFgzU👋