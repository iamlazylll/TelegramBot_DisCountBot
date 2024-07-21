import telebot
import schedule
import time
import json
import math
import threading
from datetime import datetime
import os
import pytz
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


# import pchome_crawler
with open('secret.json', 'r') as sec:
    secinfo = json.load(sec)
BOT_TOKEN = secinfo["TOKEN"]
CHAT_ID = secinfo["GROUP_ID"]
bot=telebot.TeleBot(BOT_TOKEN, parse_mode="markdown")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,f"這款Telegram bot會檢查各商城是否有優惠方案並發送優惠活動通知至您的Telegram帳號，確保您不會錯過任何優惠訊息。")
    bot.send_message(message.chat.id, f"你知道的，我並沒有智能。所以請使用以下指令來命令我： \
                        \n1. /check：主動傳送推播訊息 \
                        \n2. /re ：清空篩選器 \
                        \n3. /list ：列出所有購物網站，可用按鈕將購物網站加入篩選器 \
                        \n4. /search <商品名稱> ：使用不在篩選器的購物網站搜尋商品 \
                        \n- 例如： /search 肥皂 \
                        \n \
                        \n注意事項： \
                        \n- 您的篩選器將在使用中保存，即使在重新啟動機器人後也會保持不變。 \
                        \n- 請勿重複、頻繁輸入指令，否則將影響您的使用體驗。\
                        \n \
                        \n這不是威脅，你已經被警告過了。
                        \n-[回報連結](https://www.youtube.com/watch?v=dQw4w9WgXcQ)", disable_web_page_preview = True)
bot_info = bot.get_me()  # Fetches the bot's information
bot_name = bot_info.first_name  # Gets the bot's first name

# 儲存每個用戶的黑名單網站列表
unpreferences_file = "unpreferences.json"
unpreferences = {}

# 預設的網站清單
default_sites = [
    {"name": "蝦皮", "url": "https://shopee.tw/search?keyword="},
    {"name": "露天", "url": "https://www.ruten.com.tw/find/?q="},
    {"name": "momo", "url": "https://www.momoshop.com.tw/search/searchShop.jsp?keyword="},
    {"name": "PChome", "url": "https://24h.pchome.com.tw/search/?q="},
    {"name": "yahoo", "url": "https://tw.buy.yahoo.com/search/product?p="},
    {"name": "樂天", "url": "https://www.rakuten.com.tw/search/"},
    {"name": "酷澎coupang", "url": "https://www.tw.coupang.com/search?q="},
    {"name": "ETMall東森", "url": "https://www.etmall.com.tw/Search?keyword="},
    {"name": "松果", "url": "https://www.pcone.com.tw/search?q="}
]
# 加載黑名單
def load_unpreferences():
    global unpreferences
    if os.path.exists(unpreferences_file):
        with open(unpreferences_file, "r") as file:
            unpreferences = json.load(file)
    else:
        unpreferences = {}
# 保存黑名單
def save_unpreferences():
    with open(unpreferences_file, "w") as file:
        json.dump(unpreferences, file)

load_unpreferences()
@bot.message_handler(commands=["add"])
def add_web(message):
    user_id = str(message.from_user.id)
    if user_id not in unpreferences:
        unpreferences[user_id] = []
    site_name = message.text[5:].strip()
    for site in default_sites:
        if site_name in site["name"]:
            if site in unpreferences[user_id]:
                bot.reply_to(message, f"{site_name}已存在於你的篩選器中")
                return
            else:
                unpreferences[user_id].append(site)
                bot.reply_to(message, f"{site_name}成功加入篩選器")
                save_unpreferences()
                return
    bot.reply_to(message, "此網站不屬於我的預設清單，請透過此連結進行推薦回報。[回報連結](https://www.youtube.com/watch?v=dQw4w9WgXcQ)", disable_web_page_preview = True)

# /del 指令：將指定購物網站移出黑名單
@bot.message_handler(commands=["del"])
def delete_web(message):
    user_id = str(message.from_user.id)
    if user_id not in unpreferences:
        unpreferences[user_id] = []
    site_name = message.text[5:].strip()
    unpreferences_sites = [un["name"] for un in unpreferences[user_id]]
    for site in default_sites:
        if site_name in site["name"]:
            if site['name'] in unpreferences_sites:
                unpreferences[user_id].remove(site)
                bot.reply_to(message, f"{site['name']}成功從你的篩選器中移除")
                save_unpreferences()
                return
            else:
                bot.reply_to(message, f"{site_name}不在你的篩選器中")
                return
    bot.reply_to(message, "此網站不屬於我的預設清單，請透過此連結進行推薦回報。[回報連結](https://www.youtube.com/watch?v=dQw4w9WgXcQ)", disable_web_page_preview = True)

# /reset 指令：重置黑名單
@bot.message_handler(commands=['re'])
def list_reset(message):
    user_id = str(message.from_user.id)
    unpreferences[user_id] = []
    save_unpreferences()
    bot.reply_to(message, "重置成功")

def gen_markup(user_id):
    # user_id = str(message.from_user.id)
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    item_list = [site["name"] for site in default_sites]

    if user_id not in unpreferences.keys():
        nope_item = []
    else:
        nope_item = [un["name"] for un in unpreferences[user_id]]

    buttons = []
    for item in item_list:
        if item in nope_item:
            statu = "❌:" + item
        else:
            statu = "⭕️:" + item
        buttons.append(InlineKeyboardButton(statu, callback_data=item))

    markup.add(*buttons)
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = str(call.from_user.id)
    site_name = call.data
    if user_id not in unpreferences.keys():
        unpreferences[user_id] = []
    for site in default_sites:
        if site_name in site["name"]:
            if site in unpreferences[user_id]:
                unpreferences[user_id].remove(site)
                # bot.send_message(call.message.chat.id, f"{site['name']}成功從你的黑名單中移除")
                save_unpreferences()
                break
            else:
                unpreferences[user_id].append(site)
                # bot.send_message(call.message.chat.id, f"{site_name}成功加入黑名單")
                save_unpreferences()
                break
    bot.edit_message_reply_markup(chat_id = call.message.chat.id, message_id=call.message.message_id, reply_markup=gen_markup(str(call.from_user.id)))

# /list 指令：列出用戶的黑名單
@bot.message_handler(commands=['list'])
def list_preference(message):
    # user_id = str(message.from_user.id)
    bot.reply_to(message, f"你的篩選器在這：(⭕️代表此網站將被允許用於搜尋關鍵字，❌則反之)", reply_markup=gen_markup(str(message.from_user.id)))

# /search 指令：根據用戶偏好網站進行搜尋
@bot.message_handler(commands=["search"])
def send_search(message):
    user_id = str(message.from_user.id)
    if user_id not in unpreferences or not unpreferences[user_id]:
        user_unpreferences = []
    else:
        user_unpreferences = unpreferences[user_id]

    kwd = message.text[8:].strip()
    if not kwd:
        bot.reply_to(message, "你要給我關鍵字才能搜尋啊，我又不是什麼AI......")
        return

    bot.send_message(message.chat.id, f"正在拼老命搜尋 '{kwd}'...")
    time.sleep(0.5)
    result = ""
    all_sites = set([site['name'] for site in default_sites])
    unpreferences_sites = set([un["name"] for un in user_unpreferences])
    filtered_sites = list(all_sites - unpreferences_sites)
    for site in default_sites:
        if site['name'] in filtered_sites:
            result += f"[{site['name']}搜尋連結]({site['url']}{kwd})\n"

    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['check'])
def check_discount(message):
    discount()

def discount(): # 用戶主動
    if os.path.exists("pchome_coupon_.json"):
        with open('pchome_coupon_.json','r', encoding="utf-8") as file:
            import_information = json.load(file)
        for info in import_information:
            start=datetime.fromtimestamp(int(math.floor(float(info['startTime'])))).strftime("%Y-%m-%d, %H:%M:%S")  
            end=datetime.fromtimestamp(int(math.floor(float(info['endTime'])))).strftime("%Y-%m-%d, %H:%M:%S") 
            message = f"""商場名稱 : {info['shopName']}
        優惠種類 : {info['disCountType']}
        活動連結 : {info['shoplink']}
        活動開始日期 : {start}
        活動結束日期 : {end}
        優惠資訊 : {info['description']}""" 
            startTime = float(info['startTime'])   
            daysbefore = time.time() // 86400 - startTime // 86400    
    

            if daysbefore == 0 or daysbefore == 3:
                bot.send_message(CHAT_ID, message)

            endTime = float(info["endTime"])   
            daysleft =endTime // 86400 - time.time() // 86400  
            
            print(f"{info['description']}, {daysbefore}, {daysleft}")

            if daysleft==1 and daysbefore > 2:
                bot.send_message(CHAT_ID,"Your discount is only 1 day left!")
                bot.send_message(CHAT_ID, message)
    # lastSendTime = datetime.now(pytz.timezone('Asia/Taipei'))
    return


lash_hash = ""

def checkdailydiscount():
    global lash_hash
    if os.path.exists("pchome_coupon_.json"):
        with open('pchome_coupon_.json','r', encoding="utf-8") as file:
            import_information = json.load(file)
        current_hash = hash(json.dumps(import_information))

        if lash_hash != current_hash:
            discount()
            lash_hash = current_hash

# schedule.every().day.at("00:00").do(discount)
def run():
    bot.infinity_polling()
    pass       
def debuggingf():
    print("working...")
schedule.every(2).seconds.do(checkdailydiscount)
task = threading.Thread(target=run)
task.start()
while True:
    schedule.run_pending()
        # bot.polling()
    time.sleep(1)
# bot.infinity_polling()

# schedule.every().seconds(5).do(pchome_crawler.Crawling())



