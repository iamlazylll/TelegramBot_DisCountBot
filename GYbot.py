import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
import os
import time

with open('secret.json', 'r') as sec:
    secinfo = json.load(sec)
BOT_TOKEN = secinfo["TOKEN"]
CHAT_ID = secinfo["CHAT_ID"]
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="markdown")

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
    {"name": "樂天", "url": "https://www.rakuten.com.tw/search/="},
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

# @bot.message_handler(commands=['help'])
# def send_helping(message):
#     bot.send_message(message.chat.id, f"警告：過度依賴此機器人可能使您深陷財務危機。")
#     # bot.send_message(message.chat.id, f"...")
#     # time.sleep(0.5)
#     # bot.send_message(message.chat.id, f"......")
#     # time.sleep(0.5)
#     # bot.send_message(message.chat.id, f"............")
#     # time.sleep(1.5)
#     bot.send_message(message.chat.id, f"你知道的，我並沒有智能。所以請使用以下指令來命令我： \
#                         \n1. /add <網站名稱> ：將指定購物網站存入黑名單 \
#                         \n- 例如： /add PChome \
#                         \n2. /del <網站名稱> ：將指定購物網站移出黑名單 \
#                         \n- 例如： /del ET \
#                         \n3. /re ：重置黑名單（重置為預設） \
#                         \n4. /list ：列出黑名單（預設為全部） \
#                         \n5. /search <商品名稱> ：使用你黑名單內的購物網站搜尋商品 \
#                         \n- 例如： /search 肥皂 \
#                         \n \
#                         \n使用說明： \
#                         \n- 購物網站名稱需區分大小寫，且應包含在預設列表中的名稱部分。 \
#                         \n- 您的黑名單將在使用中保存，即使在重新啟動機器人後也會保持不變。 \
#                         \n \
#                         \n注意事項： \
#                         \n- 如果你試圖添加已經存在於黑名單中的購物網站，將不會進行重複添加。 \
#                         \n- 當你嘗試刪除不存在於黑名單中的購物網站時，將收到相應的通知訊息。\
#                         \n \
#                         \n這不是威脅，你已經被警告過了。")

# /add 指令：添加指定網站進入黑名單
@bot.message_handler(commands=["add"])
def add_web(message):
    user_id = str(message.from_user.id)
    if user_id not in unpreferences:
        unpreferences[user_id] = []
    site_name = message.text[5:].strip()
    for site in default_sites:
        if site_name in site["name"]:
            if site in unpreferences[user_id]:
                bot.reply_to(message, f"{site_name}已存在於你的黑名單中")
                return
            else:
                unpreferences[user_id].append(site)
                bot.reply_to(message, f"{site_name}成功加入黑名單")
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
                bot.reply_to(message, f"{site['name']}成功從你的黑名單中移除")
                save_unpreferences()
                return
            else:
                bot.reply_to(message, f"{site_name}不在你的黑名單中")
                return
    bot.reply_to(message, "此網站不屬於我的預設清單，請透過此連結進行推薦回報。[回報連結](https://www.youtube.com/watch?v=dQw4w9WgXcQ)", disable_web_page_preview = True)

# /reset 指令：重置黑名單
@bot.message_handler(commands=['re'])
def list_reset(message):
    user_id = str(message.from_user.id)
    unpreferences[user_id] = []
    save_unpreferences()
    bot.reply_to(message, "重置成功")

def gen_markup(message):
    user_id = str(message.from_user.id)
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    item_list = [site["name"] for site in default_sites]

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
    for site in default_sites:
        if site_name in site["name"]:
            if site in unpreferences[user_id]:
                unpreferences[user_id].remove(site)
                bot.send_message(call.message.chat.id, f"{site['name']}成功從你的黑名單中移除")
                save_unpreferences()
                return
            else:
                unpreferences[user_id].append(site)
                bot.send_message(call.message.chat.id, f"{site_name}成功加入黑名單")
                save_unpreferences()
                return

# /list 指令：列出用戶的黑名單
@bot.message_handler(commands=['list'])
def list_preference(message):
    user_id = str(message.from_user.id)
    if user_id not in unpreferences or not unpreferences[user_id]:
        bot.reply_to(message, "你的黑名單是空的！你真是個好人！")
    else:
        user_unpreferences = unpreferences[user_id]
        site_names = [site["name"] for site in user_unpreferences]
        bot.reply_to(message, f"你的黑名單如下： {', '.join(site_names)}", reply_markup=gen_markup(message))

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

bot.infinity_polling()