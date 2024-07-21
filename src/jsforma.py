import json

datsrc = "discount_events.json"
targn = "discount_testdata.json"
dic = {}
class Formating:
    def __init__(self, shopname, disctype, discdetail, link, requ, t_st, t_ed, desc, payway):
        self.shopName= shopname, 
        self.disCountType= disctype,
        self.discountDetail= discdetail,
        self.shopLink= link,
        self.requirement= requ, 
        self.startTime= t_st,
        self.endTime= t_ed,
        self.description= desc,
        self.payment_method= payway
    def to_dic(self):
        return {
            
        }
with open(datsrc, 'r', encoding='utf-8') as origins:
    