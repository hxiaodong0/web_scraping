import requests
r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs={'class':'short-desc'})
records = []
for result in results:
    first_date = result.find("strong").text[:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explaination = result.find("span", attrs={"class": 'short-truth'}).text[1:-2]
    url = result.find("a")['href']
    records.append((first_date,lie,explaination,url))
import pandas as pd
df1 = pd.DataFrame(records, columns=['date','lie','explaination',"url"])
df1.to_excel("Trump's lie.xlsx")
import os
df2 = pd.DataFrame([['a', 'b'], ['c', 'd']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
path = r'/Users/xiaodonghuo/PycharmProjects/web_scraping'
df2.to_csv(os.path.join(path, r'testing path'))