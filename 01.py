from requests_html import HTMLSession
session = HTMLSession()
url = "https://gsatcd.vercel.app/"
r = session.get(url)
r.html.render()
txt = r.html.search("學測倒數 {D} D!")["D"]
print(txt)