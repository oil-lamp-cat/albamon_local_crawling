import requests
import os
from bs4 import BeautifulSoup as bs
import time
from urllib import parse
import pandas as pd

url_s = "https://www.albamon.com/jobs/area?page=1&sortType=DEFAULT&searchPeriodType=ALL&condition=%7B%22condition%22%3A%7B%22areas%22%3A%5B%7B%22si%22%3A%22B000%22%2C%22gu%22%3A%22B090%22%2C%22dong%22%3A%22B0900130%22%2C%22name%22%3A%22%"
url_e = "%22%7D%5D%2C%22similarDongJoin%22%3Afalse%2C%22parts%22%3A%5B%5D%2C%22workPeriodTypes%22%3A%5B%5D%2C%22workWeekTypes%22%3A%5B%5D%2C%22workDayTypes%22%3A%5B%5D%2C%22workTimeTypes%22%3A%5B%5D%2C%22excludeNegoAge%22%3Afalse%2C%22employmentTypes%22%3A%5B%5D%2C%22excludeKeywords%22%3A%5B%5D%2C%22selectedArea%22%3A%7B%22si%22%3A%22%22%2C%22gu%22%3A%22%22%2C%22dong%22%3A%22%22%7D%7D%2C%22extensionCondition%22%3A%7B%22area%22%3A%7B%7D%2C%22brand%22%3A%7B%7D%2C%22franchise%22%3A%7B%7D%2C%22franchiseStore%22%3A%7B%7D%2C%22callCenter%22%3A%7B%7D%2C%22guerrilla%22%3A%7B%22guerrillaBoothTabNo%22%3A0%7D%2C%22map%22%3A%7B%22radius%22%3A120%2C%22zoom%22%3A0%7D%2C%22miniJob%22%3A%7B%7D%2C%22ongoing%22%3A%7B%7D%2C%22part%22%3A%7B%7D%2C%22pay%22%3A%7B%7D%2C%22preference%22%3A%7B%7D%2C%22recent%22%3A%7B%7D%2C%22scrap%22%3A%7B%7D%2C%22search%22%3A%7B%22disableExceptedConditions%22%3A%5B%5D%2C%22suitBannerNo%22%3A0%7D%2C%22season%22%3A%7B%7D%2C%22senior%22%3A%7B%7D%2C%22shortTerm%22%3A%7B%7D%2C%22specUp%22%3A%7B%7D%2C%22subway%22%3A%7B%7D%2C%22suit%22%3A%7B%7D%2C%22teenager%22%3A%7B%7D%2C%22town%22%3A%7B%22similarDongJoin%22%3Afalse%7D%2C%22trust%22%3A%7B%7D%2C%22university%22%3A%7B%7D%2C%22welfare%22%3A%7B%7D%2C%22albamonZ%22%3A%7B%7D%7D%7D"
url_l = parse.quote("하성면") #테스트

url_full = url_s + url_l + url_e

response = requests.get(url = url_full)
html_text = response.text
html = bs(html_text, 'html.parser')

# 전체 데이터
data = {}
# title 크롤링
title = []
title_crawled = html.select(".Typography_typography__53V55.Typography_typography--B1__O3FkV.Typography_typography--medium__EuyrE.list-item-recruit__recruit-title")
for t in title_crawled:
    ts = t.string
    title.append(ts)
# print(title)

# url 크롤링
url = []
url_crawled = html.select('.Button_button__S9rjD.Button_text__5x_Cn.Button_large___Kecx.Button_primary__5usVQ.list-item-recruit__link.list-item-recruit__link--expand.list-item-recruitgoogle-analytics')
for u in url_crawled:
    url_href = u.attrs['href']
    url.append(url_href)
# print(url)

df1 = pd.DataFrame(url)
df1.columns = ["url"]
df2 = pd.DataFrame(title)
df2.columns = ["tilte"]
df = pd.concat([df2, df1], axis = 1)

df.to_csv('./save.csv', index=False, encoding='utf-8')
print(df)