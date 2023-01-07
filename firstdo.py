from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.com/")
driver.save_screenshot("screenshot-goolgle.png")
driver.get("https://www.instagram.com/yukafumi02/")
time.sleep(10)
driver.save_screenshot("yukafumi02.png")
driver.close()