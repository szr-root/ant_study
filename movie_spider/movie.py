import json

import requests
from bs4 import BeautifulSoup
import pandas

page_indexs = range(0, 250, 25)
# page_indexs = [0]

cookies = 'll="118318"; bid=7bKGYX6iOWc; __utmc=30149280; __utmz=30149280.1639561796.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=223695111; __utmz=223695111.1639561796.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _vwo_uuid_v2=D020C87C1FEBBBCA25B86B0C5A4641768|80039c08f6f7d517144109770afda4e1; __gads=ID=8a07d3d0174a2254-2240a0ea6fcf00ed:T=1639561819:RT=1639561819:S=ALNI_MZ6TXHE-qV86w2JXksUMqNiiuw_JQ; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1206713983.1639561796.1639561796.1639622175.2; __utmb=30149280.0.10.1639622175; __utma=223695111.1424709089.1639561796.1639561796.1639622175.2; __utmb=223695111.0.10.1639622175; _pk_id.100001.4cf6=324c77dd9360ad7b.1639561796.2.1639622630.1639561819.'
cookies_dict = {cook.split('=')[0]: cook.split('=')[1] for cook in cookies.split('; ')}
print(cookies_dict)


def download_all_htmls():
    htmls = []
    for index in page_indexs:
        # https: // movie.douban.com / top250?start = 50 & filter =
        url = f'https://movie.douban.com/top250?start={index}&filter='
        header = {'Cookie': cookies,
                  'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"}
        print('craw html', url)
        r = requests.get(url, headers=header)
        if r.status_code != 200:
            raise Exception('error')
        htmls.append(r.text)
        # print(r.text)
    return htmls


def parse_single_html(html):
    """
    解析单个Html，得到数据
    :param html:
    :return:
    """
    soup = BeautifulSoup(html, 'html.parser')
    article_items = (
        soup.find('div', class_='article').find('ol', class_='grid_view')
            .find_all('div', class_='item')
    )
    # print(article_item)
    datas = []
    for article_item in article_items:
        rank = article_item.find('div', class_='pic').find('em').get_text()
        info = article_item.find('div', class_='info')
        title = info.find('div', class_='hd').find('span', class_='title').get_text()
        stars = (
            info.find('div', class_='bd')
                .find('div', class_='star')
                .find_all('span')
        )
        rating_star = stars[0]['class'][0]
        rating_num = stars[1].get_text()
        comments = stars[3].get_text()

        datas.append({
            'rank': rank,
            'title': title,
            'rating_star': rating_star.replace('rating', '').replace('-t', ''),
            'rating_num': rating_num,
            'comments': comments.replace('人评价', '')
        })

    return datas


def write_to_txt(datas):
    with open('movie.txt', 'a') as f:
        for data in datas:
            for value in data.values():
                f.write(format(value, '') + '\t')
            f.write('\n')
        f.flush()


def write_to_xls(all_datas):
    df = pandas.DataFrame(all_datas)
    print(df)
    df.to_excel('电影排名top250.xlsx')


all_datas = []
htmls = download_all_htmls()
for html in htmls:
    datas = parse_single_html(html)
    write_to_txt(datas)
    all_datas.extend(datas)
    # print(datas)
write_to_xls(all_datas)
