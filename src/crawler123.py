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
# options = webdriver.ChromeOptions()
# options.add_argument('--disable-gpu')  # 如果遇到一些 bug 可以取消 GPU 渲染
# options.add_argument('--no-sandbox')  # 取消沙盒模式

# 建立 WebDriver 服務
# service = Service(ChromeDriverManager().install())

# 啟動瀏覽器
# driver = webdriver.Chrome(service=service, options=options)

# 打開目標網頁
Cookies = {
            "Cookie": "__LOCALE__null=TW; _gcl_au=1.1.1826593991.1721307553; csrftoken=30nAQ05fQFLe5N0WcPHscvAAw8hCoEHZ; _QPWSDCXHZQA=a9ed4b2b-924b-4e5c-902b-076e22e82dff; REC7iLP4Q=12763449-2832-4f5a-b015-10ba67c42724; SPC_SI=aj6XZgAAAAB2YXBTU3NVeHO6OgAAAAAAV2JCRUtZcTY=; SPC_F=bFDKcZfLsSqIopwhiI3PdKkhVUKohOim; REC_T_ID=886d5b2e-4505-11ef-9ca5-56a2b8c59204; _fbp=fb.1.1721307554280.175103990952470194; _sapid=ba20d44a18314d2c1cb989c03f0f79de56d293be04b24f8380f6ee78; _gid=GA1.2.2070549343.1721307557; SPC_SC_SA_TK=; SPC_SC_SA_UD=; SPC_SC_OFFLINE_TOKEN=; SC_SSO=-; SC_SSO_U=-; SPC_SC_SESSION=; _med=refer; _ga_JD9WKB3ZNL=GS1.1.1721314031.2.1.1721315966.59.0.0; SPC_CLIENTID=YkZES2NaZkxzU3FJdvqpdwtwrkttgioi; SPC_U=1034563263; SPC_T_IV=QlZjaVlnVHZ0WnBBaXY1Uw==; SPC_R_T_ID=r4Tzempj/RXS+0F/yxPTAiP38O5Oq0YM98xHgmqtQ1FyfHt5i/MIRE8QJMh+oNgau2+mNS/DsnGvUXWYhayDi/n0ejelPBFPEX2MXr5grEZRidf2jLYtIullDrTZ/Uyd+MrL4VukFdSfIlYV3PDhdhJrey0RqUJDrsnjhGGgGeY=; SPC_R_T_IV=QlZjaVlnVHZ0WnBBaXY1Uw==; SPC_T_ID=r4Tzempj/RXS+0F/yxPTAiP38O5Oq0YM98xHgmqtQ1FyfHt5i/MIRE8QJMh+oNgau2+mNS/DsnGvUXWYhayDi/n0ejelPBFPEX2MXr5grEZRidf2jLYtIullDrTZ/Uyd+MrL4VukFdSfIlYV3PDhdhJrey0RqUJDrsnjhGGgGeY=; SPC_CDS_CHAT=e9511888-800a-40ed-81af-61d2d9ae3df6; SPC_EC=.c3JWSkxtUnpEZUlhY2w3OKsvyzyWHZ451G8KEfbTyFsFtzWnIFAKVqAmi+h0l3XFtggTVlqOlUGuaXo15dwoa3BFBr8+g5P93piy78OPnYytNZPmMMKiTD8BeJ4ogdwSzNc2QeeTS0e/FM4HxlxqgWRA5N6sBu7acMmoHQV9qd0Ee8orBWoGMeXjZmL7q97MuRLJtNPZFsYrt7mOuzHsXg==; SPC_ST=.c3JWSkxtUnpEZUlhY2w3OKsvyzyWHZ451G8KEfbTyFsFtzWnIFAKVqAmi+h0l3XFtggTVlqOlUGuaXo15dwoa3BFBr8+g5P93piy78OPnYytNZPmMMKiTD8BeJ4ogdwSzNc2QeeTS0e/FM4HxlxqgWRA5N6sBu7acMmoHQV9qd0Ee8orBWoGMeXjZmL7q97MuRLJtNPZFsYrt7mOuzHsXg==; AC_CERT_D=U2FsdGVkX1/6UiysEmVJWqpCm/F2ArVLpF0Ie+9w1yHt4ZeXOlSpk0QshMbTtv1CFPhoSRymi13VUJYeDDqP1UA7ixXXh6XF0W402NEuRdclV/RFeZ+p6p+cNEilxO64aoUhhc536S2uQnkJceOvVXBh7+gpsXSCuBt62wnomDIQ9pWzZ3Or/OGgYeFb+7kC1mPzTMOrv1uEfhuEc54ky1AOA0qnbweKN0eatEMBYxk11BQk1xDKFrpZfRXeL/banGfE8AAaHO0gFLPJ5F0P5A==; SPC_SEC_SI=v1-RWxGZzhjRVVFQVBpQmg0eAuAXOiDZtVL8Gim99VSEUG0koKt9jMg5maOdGT41gIcuRMEm5uyU0r3tP2PHTB2HWtWP+3zJYrdRZVIXDylXUs=; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.1.126026147.1721307557; _dc_gtm_UA-61915057-6=1; shopee_webUnique_ccd=YXyfeCIiZ%2BhuUi%2FKf9ooVw%3D%3D%7C40rsmvDeReTidPa7qxj5QN9yMRjvxSQaorWaAeJkoJzAmkLdb5c2%2B2qeuM0jwXZQ25V%2BKVkAShjk8Q%3D%3D%7CQ2c3CKhGLkVnQRS8%7C08%7C3; ds=c98e5a3b89a68971fdd9e13a20e816c6; _ga_E1H7XE0312=GS1.1.1721434433.9.1.1721436336.13.0.0",
}
headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
          "Cookies": "__LOCALE__null=TW; _gcl_au=1.1.1826593991.1721307553; csrftoken=30nAQ05fQFLe5N0WcPHscvAAw8hCoEHZ; _QPWSDCXHZQA=a9ed4b2b-924b-4e5c-902b-076e22e82dff; REC7iLP4Q=12763449-2832-4f5a-b015-10ba67c42724; SPC_SI=aj6XZgAAAAB2YXBTU3NVeHO6OgAAAAAAV2JCRUtZcTY=; SPC_F=bFDKcZfLsSqIopwhiI3PdKkhVUKohOim; REC_T_ID=886d5b2e-4505-11ef-9ca5-56a2b8c59204; _fbp=fb.1.1721307554280.175103990952470194; _sapid=ba20d44a18314d2c1cb989c03f0f79de56d293be04b24f8380f6ee78; _gid=GA1.2.2070549343.1721307557; SPC_SC_SA_TK=; SPC_SC_SA_UD=; SPC_SC_OFFLINE_TOKEN=; SC_SSO=-; SC_SSO_U=-; SPC_SC_SESSION=; _med=refer; _ga_JD9WKB3ZNL=GS1.1.1721314031.2.1.1721315966.59.0.0; SPC_CLIENTID=YkZES2NaZkxzU3FJdvqpdwtwrkttgioi; SPC_U=1034563263; SPC_T_IV=QlZjaVlnVHZ0WnBBaXY1Uw==; SPC_R_T_ID=r4Tzempj/RXS+0F/yxPTAiP38O5Oq0YM98xHgmqtQ1FyfHt5i/MIRE8QJMh+oNgau2+mNS/DsnGvUXWYhayDi/n0ejelPBFPEX2MXr5grEZRidf2jLYtIullDrTZ/Uyd+MrL4VukFdSfIlYV3PDhdhJrey0RqUJDrsnjhGGgGeY=; SPC_R_T_IV=QlZjaVlnVHZ0WnBBaXY1Uw==; SPC_T_ID=r4Tzempj/RXS+0F/yxPTAiP38O5Oq0YM98xHgmqtQ1FyfHt5i/MIRE8QJMh+oNgau2+mNS/DsnGvUXWYhayDi/n0ejelPBFPEX2MXr5grEZRidf2jLYtIullDrTZ/Uyd+MrL4VukFdSfIlYV3PDhdhJrey0RqUJDrsnjhGGgGeY=; SPC_CDS_CHAT=e9511888-800a-40ed-81af-61d2d9ae3df6; SPC_EC=.c3JWSkxtUnpEZUlhY2w3OKsvyzyWHZ451G8KEfbTyFsFtzWnIFAKVqAmi+h0l3XFtggTVlqOlUGuaXo15dwoa3BFBr8+g5P93piy78OPnYytNZPmMMKiTD8BeJ4ogdwSzNc2QeeTS0e/FM4HxlxqgWRA5N6sBu7acMmoHQV9qd0Ee8orBWoGMeXjZmL7q97MuRLJtNPZFsYrt7mOuzHsXg==; SPC_ST=.c3JWSkxtUnpEZUlhY2w3OKsvyzyWHZ451G8KEfbTyFsFtzWnIFAKVqAmi+h0l3XFtggTVlqOlUGuaXo15dwoa3BFBr8+g5P93piy78OPnYytNZPmMMKiTD8BeJ4ogdwSzNc2QeeTS0e/FM4HxlxqgWRA5N6sBu7acMmoHQV9qd0Ee8orBWoGMeXjZmL7q97MuRLJtNPZFsYrt7mOuzHsXg==; AC_CERT_D=U2FsdGVkX1/6UiysEmVJWqpCm/F2ArVLpF0Ie+9w1yHt4ZeXOlSpk0QshMbTtv1CFPhoSRymi13VUJYeDDqP1UA7ixXXh6XF0W402NEuRdclV/RFeZ+p6p+cNEilxO64aoUhhc536S2uQnkJceOvVXBh7+gpsXSCuBt62wnomDIQ9pWzZ3Or/OGgYeFb+7kC1mPzTMOrv1uEfhuEc54ky1AOA0qnbweKN0eatEMBYxk11BQk1xDKFrpZfRXeL/banGfE8AAaHO0gFLPJ5F0P5A==; SPC_SEC_SI=v1-RWxGZzhjRVVFQVBpQmg0eAuAXOiDZtVL8Gim99VSEUG0koKt9jMg5maOdGT41gIcuRMEm5uyU0r3tP2PHTB2HWtWP+3zJYrdRZVIXDylXUs=; _ga_E1H7XE0312=GS1.1.1721438516.10.1.1721438519.57.0.0; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.126026147.1721307557; shopee_webUnique_ccd=rN5dEVMHlijCg7oFpCvh9w%3D%3D%7CHkrsmvDeReTidPa7qxj5QN9yMRjvxSQaorWaAQLwhpzAmkLdb5c2%2B2qeuM0jwXZQ25V%2BKVkAShjk8Q%3D%3D%7CQ2c3CKhGLkVnQRS8%7C08%7C3; ds=26e3612436ede85587074ddf234642b1",
          "Af-Ac-Enc-Sz-Token": "rN5dEVMHlijCg7oFpCvh9w==|HkrsmvDeReTidPa7qxj5QN9yMRjvxSQaorWaAQLwhpzAmkLdb5c2+2qeuM0jwXZQ25V+KVkAShjk8Q==|Q2c3CKhGLkVnQRS8|08|3",
          "Referer": "https://shopee.tw/campaigns"
}
payload = {
            "campaign_collection_id": "0",
            "campaign_entry_type": "All campaign page",
            "hide_ended_campaign": "true",
            "hide_scheduled_campaign": "true",
            "limit": "9",
            "offset": "0",
            "show_collection_info": "false"
}

# cookielist = {
#     '__LOCALE__null'='TW', 
#     '_gcl_au'='1.1.1826593991.1721307553', 
#     'csrftoken'='30nAQ05fQFLe5N0WcPHscvAAw8hCoEHZ',
#     '_QPWSDCXHZQA'='a9ed4b2b-924b-4e5c-902b-076e22e82dff',
#     'REC7iLP4Q'='12763449-2832-4f5a-b015-10ba67c42724', 
#     'SPC_SI'='aj6XZgAAAAB2YXBTU3NVeHO6OgAAAAAAV2JCRUtZcTY=',
#     'SPC_F'='bFDKcZfLsSqIopwhiI3PdKkhVUKohOim',
#     'REC_T_ID'='886d5b2e-4505-11ef-9ca5-56a2b8c59204', _fbp=fb.1.1721307554280.175103990952470194; _sapid=ba20d44a18314d2c1cb989c03f0f79de56d293be04b24f8380f6ee78; _gid=GA1.2.2070549343.1721307557; SPC_SC_SA_TK=; SPC_SC_SA_UD=; SPC_SC_OFFLINE_TOKEN=; SC_SSO=-; SC_SSO_U=-; SPC_SC_SESSION=; _med=refer; _ga_JD9WKB3ZNL=GS1.1.1721314031.2.1.1721315966.59.0.0; SPC_CLIENTID=YkZES2NaZkxzU3FJdvqpdwtwrkttgioi; SPC_U=1034563263; SPC_T_IV=QlZjaVlnVHZ0WnBBaXY1Uw==; SPC_R_T_ID=r4Tzempj/RXS+0F/yxPTAiP38O5Oq0YM98xHgmqtQ1FyfHt5i/MIRE8QJMh+oNgau2+mNS/DsnGvUXWYhayDi/n0ejelPBFPEX2MXr5grEZRidf2jLYtIullDrTZ/Uyd+MrL4VukFdSfIlYV3PDhdhJrey0RqUJDrsnjhGGgGeY=; SPC_R_T_IV=QlZjaVlnVHZ0WnBBaXY1Uw==; SPC_T_ID=r4Tzempj/RXS+0F/yxPTAiP38O5Oq0YM98xHgmqtQ1FyfHt5i/MIRE8QJMh+oNgau2+mNS/DsnGvUXWYhayDi/n0ejelPBFPEX2MXr5grEZRidf2jLYtIullDrTZ/Uyd+MrL4VukFdSfIlYV3PDhdhJrey0RqUJDrsnjhGGgGeY=; SPC_CDS_CHAT=e9511888-800a-40ed-81af-61d2d9ae3df6; SPC_EC=.c3JWSkxtUnpEZUlhY2w3OKsvyzyWHZ451G8KEfbTyFsFtzWnIFAKVqAmi+h0l3XFtggTVlqOlUGuaXo15dwoa3BFBr8+g5P93piy78OPnYytNZPmMMKiTD8BeJ4ogdwSzNc2QeeTS0e/FM4HxlxqgWRA5N6sBu7acMmoHQV9qd0Ee8orBWoGMeXjZmL7q97MuRLJtNPZFsYrt7mOuzHsXg==; SPC_ST=.c3JWSkxtUnpEZUlhY2w3OKsvyzyWHZ451G8KEfbTyFsFtzWnIFAKVqAmi+h0l3XFtggTVlqOlUGuaXo15dwoa3BFBr8+g5P93piy78OPnYytNZPmMMKiTD8BeJ4ogdwSzNc2QeeTS0e/FM4HxlxqgWRA5N6sBu7acMmoHQV9qd0Ee8orBWoGMeXjZmL7q97MuRLJtNPZFsYrt7mOuzHsXg==; AC_CERT_D=U2FsdGVkX1/6UiysEmVJWqpCm/F2ArVLpF0Ie+9w1yHt4ZeXOlSpk0QshMbTtv1CFPhoSRymi13VUJYeDDqP1UA7ixXXh6XF0W402NEuRdclV/RFeZ+p6p+cNEilxO64aoUhhc536S2uQnkJceOvVXBh7+gpsXSCuBt62wnomDIQ9pWzZ3Or/OGgYeFb+7kC1mPzTMOrv1uEfhuEc54ky1AOA0qnbweKN0eatEMBYxk11BQk1xDKFrpZfRXeL/banGfE8AAaHO0gFLPJ5F0P5A==; SPC_SEC_SI=v1-RWxGZzhjRVVFQVBpQmg0eAuAXOiDZtVL8Gim99VSEUG0koKt9jMg5maOdGT41gIcuRMEm5uyU0r3tP2PHTB2HWtWP+3zJYrdRZVIXDylXUs=; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.1.126026147.1721307557; _dc_gtm_UA-61915057-6=1; shopee_webUnique_ccd=YXyfeCIiZ%2BhuUi%2FKf9ooVw%3D%3D%7C40rsmvDeReTidPa7qxj5QN9yMRjvxSQaorWaAeJkoJzAmkLdb5c2%2B2qeuM0jwXZQ25V%2BKVkAShjk8Q%3D%3D%7CQ2c3CKhGLkVnQRS8%7C08%7C3; ds=c98e5a3b89a68971fdd9e13a20e816c6; _ga_E1H7XE0312=GS1.1.1721434433.9.1.1721436336.13.0.0

# }
url_ = 'https://shopee.tw/api/v4/campaign_collection/get_campaign_list?campaign_collection_id=0&campaign_entry_type=All%20campaign%20page&hide_ended_campaign=true&hide_scheduled_campaign=true&limit=9&offset=0&show_collection_info=false'
# driver.get(url)
webd = requests.get(url = url_, params=payload,headers=headers, cookies=Cookies)
webd.encoding = 'gzip'
print(webd.json())
# 獲取網頁的 HTML
# html = driver.page_source


# 將 HTML 儲存到文件中
# with open('page.html', 'w', encoding='utf-8') as file:
#     file.write(html)


# print("網頁 HTML 已經成功爬取並儲存到 'page.html'。瀏覽器將保持開啟狀態。")
