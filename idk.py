import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.instagram.com/yukafumi02/")
soup = BeautifulSoup(response.text, "html.parser")
for link in soup.find_all("src"):
    print(link)