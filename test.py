from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options=Options()
options.chrome_executable_path="D:\sandy\code\chromedriver.exe"
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.save_screenshot("screenshot-goolgle.png")
driver.get("https://www.instagram.com/yukafumi02/")
time.sleep(10)
driver.save_screenshot("yukafumi02.png")
driver.close()