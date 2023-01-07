from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import wget
import os 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/")
username=  WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
username.clear()
password.clear()
keyword= "yukafumi"
username.send_keys("prolin1030@yahoo.com.tw")
password.send_keys("gogo1030")
password.send_keys(Keys.RETURN)
time.sleep(5)
next = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@type="button"]'))
    )
driver.get("https://www.instagram.com/yukafumi02/")
name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "yukafumi02"))
    )
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME,'img'))
    )
images = driver.find_elements(By.TAG_NAME,'img')
images = [image.get_attribute('src') for image in images]
path = os.getcwd()
path = os.path.join(path,keyword[0:])
os.mkdir(path)
print(path)
count=0
for image in images:
    save_as= os.path.join(path,keyword[0:]+ str(count)+'.jpg')
    wget.download(image,save_as)
    count += 1