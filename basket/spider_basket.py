import requests


months = ['%02d' % month for month in range(1, 13)]

with open('match.txt', 'w+') as f:
      for month in months:
            if month in ['01','03','05','07','08','10','12']:
                  day = 31
            else:
                  day = 30
            if month == '02':
                  day = 28
            url = f'https://webapi.sporttery.cn/gateway/jc/basketball/getMatchResultV1.qry?' \
            f'matchPage=1&matchBeginDate=2021-{month}-01&matchEndDate=2021-{month}-{day}&leagueId=&pageSize=900' \
            '&pageNo=1&isFix=0&pcOrWap=1'
            r = requests.get(url)
            matchs = r.json()['value']['matchResult']
            f.write('#' * 30 + f'第{month}月' + '#' * 30 + '\n')
            for i in range (0,len(matchs)):
                  match = matchs[i]
                  matchData = match['matchDate']
                  matchNumStr = match['matchNumStr']
                  leagueNameAbbr = match['leagueNameAbbr']
                  home_allaway = str([match['awayTeam']+'  VS  '+match['homeTeam']])
                  first_time = str([match['oneScore'],match['twoScore']])
                  second_time = str([match['threeScore'],match['fourScore']])
                  extraScore = match['extraScore']
                  finalScore = match['finalScore']
                  a = match['a']
                  goalline = match['goalline']
                  h = match['h']
                  winFlag = match['matchResultStatus']
                  f.write(matchData+'\t'+matchNumStr+'\t'+leagueNameAbbr+'\t'+home_allaway+'\t'+first_time+'\t'+second_time+'\t'+extraScore+'\t'+finalScore+'\t'+a+'\t'+goalline+'\t'+h+'\t'+winFlag+'\n')
                  f.flush()

import pandas
df = pandas.read_csv(
      './match.txt',
      sep='\t',
      header=None,
      names=['赛事日期','赛事编号','联赛','客队 vs 主队','上半时','下半时','加时赛比分','终场比分','让分主负','让分','让分主胜','状态']
                     )
df.to_excel('./result.xlsx')
