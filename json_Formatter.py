import json
import time
from datetime import datetime
import pchome_crawler
import schedule
# import threading
import pytz
# class AccountingEntry:
#     def __init__(self, shop_name, links, item_type, timestamp_e, desc=None, requ=None, paymthd=None, timestamp_s=None, descr=None, year=None, month=None, day=None):
#         self.shop_name = shop_name
#         self.links = links
#         self.desc = desc
#         self.item_type = item_type
#         self.requ = requ
#         self.timestamp_e = timestamp_e
#         self.timestamp_s = timestamp_s
#         self.paymthd = paymthd
#         self.descr = descr
#         self.year = datetime.now().year
#         self.month = datetime.now().month
#         self.day = datetime.now().day

#     # def __str__(self):
#     #     return f"[{self.item_type}] {self.shop_name}: ${self.desc} at {self.year}/{self.month}/{self.day} {self.timestamp}"
    
#     def to_dict(self):
#         return {
#             "shopName": self.shop_name, 
#             "disCountType": self.item_type,
#             "discountDetail": self.desc,
#             "shopLink": self.links,
#             "requirement": self.requ, 
#             "startTime": self.timestamp_s,
#             "endTime": self.timestamp_e,
#             "description": self.descr,
#             "payment_method": self.paymthd
#         }
# class DataFormatter:
#     def __init__(self):
#         self.accouting_book = []

#     def add_entry(self, item_name, cost, item_type):
#         entry = AccountingEntry(item_name, cost, item_type)
#         self.accouting_book.append(entry)

#     def get_total_cost(self):
#         return sum(entry.cost for entry in self.accouting_book)
    
#     def add_entry_from_dict(self, entry_dict):
#         entry = AccountingEntry(
#             item_name=entry_dict["shop_name"],
#             links=entry_dict["links"],
#             item_type=entry_dict["item_type"],
#             timestamp_s=entry_dict["timestamp_s"],
#             timestamp_e=entry_dict["timestamp_e"],
#             year=entry_dict["year"],
#             month=entry_dict["month"],
#             day=entry_dict["day"]
#         )
#         self.accouting_book.append(entry)

#     def get_entries_by_type(self, item_type):
#         return [entry for entry in self.accouting_book if entry.item_type == item_type]

#     def get_entries_by_name(self, item_name):
#         return [entry for entry in self.accouting_book if entry.item_name == item_name]

#     def to_dict(self):
#         return [entry.to_dict() for entry in self.accouting_book]
#     def get_history_str(self):
#         # return "\n".join(str(entry) for entry in self.accouting_book)
#         history_str = ""
#         for entry in self.accouting_book:
#             history_str += str(entry) + "\n"
#         return history_str

# dic = {}
# with open('discount_events.json', 'r', encoding='utf-8') as fis:
#     dic = json.load(fis)
    
#     # for i in dat:
#     #     dic[
    
#     print(dat)
# with open('discount_testdata.json', 'w', encoding='utf-8') as tesf:
#     # json.dump(dic, tesf, indent=4)
#     for dar in dic["data"]["campaigns"]:
#         tesf["startTime"].append(dar)
#         # tesf["startTime"] = dar["data"]["campaigns"]["campaign_start_time"]
# pchome_crawler.Crawling()
def formatjson():
    pchome_crawler.Crawling()
    with open("pchome_coupon.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    lst = []
    for dat in data:
        # print(dat.keys())
        start_date_str = dat["UseStartDate"]
        date_format = "%Y/%m/%d %H:%M:%S"

        # 将字符串转换为 datetime 对象
        timez = pytz.timezone('Asia/Taipei')
        start_date_obj = datetime.strptime(start_date_str, date_format).replace(tzinfo=timez)
        end_date_str = dat["UseEndDate"]

        # 将字符串转换为 datetime 对象
        end_date_obj = datetime.strptime(end_date_str, date_format).replace(tzinfo=timez)
        # sttime.replace("\/", "-")
        # sttime.replace(" ", "-")
        # sttime.replace(":", "-")
        # datetime()
        lst.append({
            "shopName": "Pchome",
            "disCountType": "coupon",
            "discountDetail": "",
            "shoplink": "https://24h.pchome.com.tw/activity/coupon",
            "requirement": "", 
            "startTime": int(start_date_obj.timestamp()), #
            "endTime": int(end_date_obj.timestamp()), #
            "startTimeDate": dat["UseStartDate"],
            "endTimeDate": dat["UseEndDate"],
            "description": dat["ActName"],
            "payment_method": ""
        })
    with open("pchome_coupon_.json", 'w', encoding="utf-8") as ff:
        json.dump(lst, ff, ensure_ascii=False, indent=4)
        # json.dump(dat, ff, indent=4)
def timing():
    formatjson()
schedule.every(1).second.do(timing)
# schedule.add()

# task = threading.Thread(target=timing)
# timer = threading.Timer(1, task)
# timer.start()
# def timing():
#     # pchome_crawler.Crawling()
#     global timer
#     # timer = threading.Timer(waiting_time, timing)
#     timer.start()
while True:
    schedule.run_pending()
    time.sleep(0.1)
# print(data[0])