import requests
from bs4 import BeautifulSoup
import pandas as pd

# tickers = ["AAPL","FB","CSCO","INFY.NS","3988.HK"]
key_statistics = {}

# testing, we can scarp any table very easily but yahoo finance is never an easy cake

# for ticker in tickers:
url = "https://tv.dhan.co/"

headers = {"User-Agent" : "Chrome/96.0.4664.110"}
page = requests.get(url, headers=headers)
page_content = page.content
soup = BeautifulSoup(page_content,"html.parser")
tabl = soup.find_all("div" , {"class" : "Mb(10px) smartphone_Pend(0px) Pend(20px)"})

temp_stats = {}
for t in tabl:
    rows = t.find_all("tr")
    for row in rows:
        # print(row.get_text())
        temp_stats[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[-1]
print(temp_stats)