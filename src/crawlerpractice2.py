from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
from bs4 import BeautifulSoup

# Path to your WebDriver executable
# driver_path = '/path/to/chromedriver'

# Configure the WebDriver
options = Options()
options.headless = True  # Run browser in headless mode (no GUI)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()

# Open the webpage
driver.get('https://24h.pchome.com.tw/activity/coupon')

# Wait for the JavaScript to execute (you might need to adjust the sleep duration)
driver.implicitly_wait(1)  # seconds

# Get the page source after JavaScript execution
html = driver.page_source

# Parse the page source with BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')
with open("crawlerprac3.html", 'w', encoding='utf-8') as fsfs:
    fsfs.write(html)

# Don't forget to quit the driver
driver.quit()
