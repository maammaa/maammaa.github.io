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
print(posts)
for i in range(6):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
images = driver.find_elements(By.CSS_SELECTOR,"img[class='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3']")    
path = os.path.join(keyword)
os.mkdir(path)
count =1
for image in images:
    save_as= os.path.join(path, keyword+'-'+str(count)+'.jpg')
    print(image.get_attribute('src'))
    wget.download(image.get_attribute('src'),save_as)
    count+=1
driver.close()