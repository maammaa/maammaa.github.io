from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import wget
import os 
import json
path1="D:\sandy\code\chromedriver.exe" #chormedriver路徑
driver = webdriver.Chrome(path1)
driver.get("https://www.instagram.com/yukafumi02/")
with open('ig.json', 'r') as f:
    data = json.loads(f.read())
for c in data:
    driver.add_cookie(c)
driver.refresh()
time.sleep(5)
keyword= "yukafumi02" #搜尋關鍵字
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.TAG_NAME,'img'))
    )
posts = int(driver.find_element(By.CSS_SELECTOR,"span[class ='_ac2a']").text) #貼文數
for i in range(6):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
links = driver.find_elements(By.CSS_SELECTOR,"[class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd']")    
# path = os.path.join(keyword)
# os.mkdir(path)
count =1
with open('linking.txt' , mode="w") as file: #清空檔案
    file.truncate(0)
for link in links:
    with open('linking.txt' , mode="a") as file:
        file.write(link.get_attribute('href')+"\n")
    count+=1
driver.close()
#<a class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd