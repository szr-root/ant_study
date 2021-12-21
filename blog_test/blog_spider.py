from utils import url_manager
from bs4 import BeautifulSoup
import requests
import re

# root_url
root_url = 'http://www.crazyant.net/'

# 初始化url_manager用来管理url
url_list = url_manager.UrlManger()
url_list.add_url(root_url)


# 用来写数据
fout = open('spider.txt', 'w')

while url_list.has_new_url():
    curent_url = url_list.get_url()
    try:
        r = requests.get(curent_url, timeout=3)
    except:
        print(curent_url, '  time out')
        if len(url_list.new_urls) == 0 :
            print('再次请求:', curent_url)
            r = requests.get(curent_url, timeout=5)
    if r.status_code != 200:
        print('requests code is not 200')
        continue
    soup = BeautifulSoup(r.text, 'html.parser')
    # 提取title
    title = soup.title.string
    fout.write('%s\t%s\n' % (curent_url, title))
    #刷新内存
    fout.flush()
    print('%s  %s  %s' % (curent_url, title, url_list.new_urls))

    # 查找页面里其他的 a 标签
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href is None:
            continue
        pattern = r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern, href):
            url_list.add_url(href)


fout.close()

#
# if __name__ == '__main__':
#     r = requests.get(url=root_url)
#     print(r.text)
