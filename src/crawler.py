# import requests
# import json
# from bs4 import BeautifulSoup
# import telebot

# # 輸入你的 Telegram Bot API Token 和你的 Telegram 聯絡 ID（可以是你的用戶 ID 或群組 ID）
# fs = open('secret.json')
# tken = json.load(fs)
# # 設置 Telegram Bot
# bot = telebot.TeleBot(tken["Secrets"]["TOKEN"], parse_mode=None)
# header = {"user-agent": 
#           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
# # 定義獲取優惠的函數

# url = 'https://shopee.tw/m/superdeals'  # 替換成你想抓取的購物網站的 URL
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup)
# # 假設優惠信息在 class="discount" 的元素中
# discount_elements = soup.find_all(class_="zFFgzU")
# # print(discount_elements)  
# for dd in discount_elements:
#     print(dd.text)

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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
# 設定 Chrome 選項
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')  # 如果遇到一些 bug 可以取消 GPU 渲染
options.add_argument('--no-sandbox')  # 取消沙盒模式

# 建立 WebDriver 服務
service = Service(ChromeDriverManager().install())

# 啟動瀏覽器
driver = webdriver.Chrome(service=service, options=options)

# 打開目標網頁
url = 'https://shopee.tw/m/dyson-mdd-0720'
driver.get(url)

# 獲取網頁的 HTML
html = driver.page_source


# 將 HTML 儲存到文件中
with open('page.html', 'w', encoding='utf-8') as file:
    file.write(html)


print("網頁 HTML 已經成功爬取並儲存到 'page.html'。瀏覽器將保持開啟狀態。")
