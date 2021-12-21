from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.baidu.com')
r.encoding = 'utf-8'
html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

links = soup.find_all('a')

for link in links:
    # print(link)
    print(link.name, link['href'], link.get_text())

print('#'*30)

pics = soup.find_all('img')
for pic in pics:
    print(pic['src'])