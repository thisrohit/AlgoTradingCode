import requests
from bs4 import BeautifulSoup
import pandas as pd

tickers = ["AAPL", "FB", "CSCO", "INFY.NS", "3988.HK"]
income_statement_dict = {}
balance_sheet_dict = {}
cash_flow_dict = {}

for ticker in tickers:
    #scrapping income statemtns
    url = "https://finance.yahoo.com/quote/{}/financials?p={}".format(ticker,ticker)
    income_statement = {}
    table_title = {}
    
    headers = {"User-Agent" : "Chrome/96.0.4664.110"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    tabl = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        heading = t.find_all("div", {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})  
        for top_row in heading:
            table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]
        rows = t.find_all("div", {"class" : "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            income_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]
    
    temp = pd.DataFrame(income_statement).T
    temp.columns = table_title["Breakdown"]
    income_statement_dict[ticker] = temp
    
print(income_statement_dict)