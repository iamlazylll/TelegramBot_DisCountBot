import requests
# from bs4 import BeautifulSoup
# import time
# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
# import threading
import json
waiting_time = 10
def Crawling():
    url_getclass = "https://ecapi.pchome.com.tw/marketing/coupon/v3/collection/coupon?"
    req_getclass = requests.get(url=url_getclass)
    classDic = req_getclass.text
    classDic2 = classDic.replace("'", "")
    #   dictionary = {}
    with open('classDic.json', 'w') as file:
        json.dump(classDic2, file, indent=4)
    with open('classDic.json', 'r') as file:
        dat = json.load(file)
    json_object = json.loads(dat)
    # print(type(json_object))
    with open('classDic.json', 'w') as file:
        json.dump(json_object, file, indent=4)

    url = "https://ecapi.pchome.com.tw/marketing/coupon/v3/collection/coupon?actid="
    url_p2 = "&&_callback=callback_coupon&callback=callback_coupon"
    final_url = ""
    url_mid = ""
    with open('classDic.json', 'r') as file:
        dat = json.load(file)
        # print(dat["Rows"])

        for d in dat["Rows"]:
            url_mid += d["ActId"]
            url_mid += ","
        url_mid = url_mid[0:len(url_mid) - 1]
        # for dat["Rows"] in dat:
        #     url_mid += dat["Rows"]["ActId"]
    # print(url_mid)
    final_url += url + url_mid + url_p2
    # print(final_url)
    req2 = requests.get(url=final_url)
    finaltxt = req2.text
    finaltxt = finaltxt[20:len(finaltxt)]
    finaltxt = finaltxt[0:len(finaltxt) - 48]

    # print(type(finaltxt))
    # print(finaltxt[0:10])
    # print(type(json.loads(finaltxt)))
    with open('pchome_coupon.json', 'w', encoding="utf-8") as file:
        json.dump(json.loads(finaltxt), file, ensure_ascii=False, indent=4)
    print("完成")


# scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
# scheduler.add_job(Crawling, 'interval', seconds=10)
# scheduler.start()
# print("排程開始")
# while True:
#     time.sleep(10)
#     print('執行中...')
#     exit()
# with open('pchome_coupon.json', 'w') as file:
#     json.dump(finaltxt, file, indent=4)
# with open('pchome_coupon.json', 'r') as file:
#     dat = json.load(file)
# json_object = json.loads(dat)
# print(type(json_object))
# with open('pchome_coupon.json', 'w') as file:
#     json.dump(json_object, file, ensure_ascii=False, indent=4)
# # final_url +=
# with open('classDic.json', 'w') as file:
#     json.dump(dat, file)


    # for i in dat:
    #     dictionary[i.split(":")[0].strip('\'').replace("\"", "")] = i.split(":")[1].strip('"\'')
            
# print(dat)
# print(classDic)
# classList.append(classDic["Rows"])
# classList = classDic["Rows"]
# print(classList)