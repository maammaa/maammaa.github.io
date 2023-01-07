from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import wget
import os 

path1="D:\sandy\code\chromedriver.exe" #chormedriver路徑
driver = webdriver.Chrome(path1)
driver.get("https://www.instagram.com/")
username=  WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
username.clear()
password.clear()
keyword= "yukafumi02" #搜尋關鍵字
username.send_keys("testerprograming2@gmail.com") #測試用帳號
password.send_keys("tester2222") #測試用密碼
password.send_keys(Keys.RETURN)
next = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@type="button"]'))
    )
search_box= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div'))
    ).click()
time.sleep(5)
search= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input'))
)
cookie = driver.get_cookies()
with open('ig.json', 'w') as f:
    f.write(json.dumps(cookie))
search.clear()
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(3)
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.TAG_NAME,'img'))
    )
posts = int(driver.find_element(By.CSS_SELECTOR,"span[class ='_ac2a']").text) #貼文數
print(posts)
scroller= int((posts-9)/6) #好像沒有用的數值QQ
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