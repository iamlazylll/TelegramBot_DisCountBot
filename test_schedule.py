import schedule
def debuggingf():
    print("working...")
schedule.every(2).seconds.do(debuggingf)
# schedule.every().seconds(5).do(pchome_crawler.Crawling())
while True:
    schedule.run_pending()