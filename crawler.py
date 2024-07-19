import requests
import json
from bs4 import BeautifulSoup
import telebot

# 輸入你的 Telegram Bot API Token 和你的 Telegram 聯絡 ID（可以是你的用戶 ID 或群組 ID）
fs = open('secret.json')
tken = json.load(fs)
# 設置 Telegram Bot
bot = telebot.TeleBot(tken["Secrets"]["TOKEN"], parse_mode=None)

# 定義獲取優惠的函數

url = 'https://shopee.tw/m/superdeals'  # 替換成你想抓取的購物網站的 URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# 假設優惠信息在 class="discount" 的元素中
discount_elements = soup.find_all(class_="zFFgzU")
# print(discount_elements)
for dd in discount_elements:
    print(dd.text)

# discount_info = []
# for element in discount_elements:
#     # discount_info.append(element.get_text(strip=True))
#     print(element)



# 定義發送優惠的函數
# def send_discount(upda    te, context):
#     discount_info = fetch_discount_info()
#     if discount_info:
#         bot.send_message(chat_id=CHAT_ID, text=discount_info)
#     else:
#         bot.send_message(chat_id=CHAT_ID, text='No discount information available.')

# 設置 Telegram Bot 的指令處理
# def main():
#     updater = Updater(token=API_TOKEN, use_context=True)
#     dp = updater.dispatcher
    
#     dp.add_handler(CommandHandler('discount', send_discount))
    
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()fetch_discount_info()

#//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div[8]/div/div/div/div/div/div/div/div[3]/div[2]/div[2]/span