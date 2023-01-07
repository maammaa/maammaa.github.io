import json 
from selenium import webdriver
path1="D:\sandy\code\chromedriver.exe" #chormedriver路徑
driver = webdriver.Chrome(path1)
cookie = driver.get_cookies()
with open('ig.json', 'w') as f:
    f.write(json.dumps(cookie))
with open('ig.json', 'r') as f:
    data = json.loads(f.read())
for c in data:
    driver.add_cookie(c)
driver.refresh()