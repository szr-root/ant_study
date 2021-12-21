import json
import pandas as pd

import requests
from bs4 import BeautifulSoup

months = ['%d' % month for month in range(1, 13)]

with open('wheather.txt', 'a') as f:
    for month in months:
        print('请求第%s个月' % month)
        r = requests.get(
            f'http://tianqi.2345.com/Pc/GetHistory?areaInfo%5BareaId%5D=71988&areaInfo%5BareaType%5D=2&date%5Byear%5D=2020&date%5Bmonth%5D={month}')
        res = json.loads(r.text)
        soup = BeautifulSoup(res['data'], 'html.parser')
        temp_node1 = soup.find('table')
        temp_node2 = soup.find('table',class_='history-table')
        trs = temp_node1.find_all('tr')[1:]
        # print(trs)
        for tr in trs:
            values = tr.find_all('td')
            # print(values)
            time = values[0].get_text().split(' ')[0]
            high = values[1].get_text()
            low = values[2].get_text()
            weather = values[3].get_text()
            wind = values[4].get_text()
            quality = values[5].find('span').get_text()
            print(time, high, low)
            # f.write(f'{time}\t{high}\t{low}\t{weather}\t{wind}\t{quality}\n')
            # f.flush()
            # df = pd.DataFrame((time,high,low,weather,wind,quality))
            df = pd.loc((time,high,low,weather,wind,quality))
            print(df)

# print(temp_node2)
