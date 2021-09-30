import requests
from bs4 import BeautifulSoup

URL = "https://fp.lhv.ee/market/balticView?locale=et"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("tr", class_="alt")

# positive = results.find_all('td')
# print(positive)
# print(results)
# for element in elements:
#     print(element)
thisDict= {}

def getStockChange(changeList):
    for value in changeList:
        return value.text.strip()

for elements in results:
    # print(elements)
    stockSymbol = elements.find('a', class_="stock-symbol")
    stockTitle = elements.find('a', class_="stock-title")
    # print(stockTitle.text)
    # print(stockSymbol.text)


    positiveChangeList = elements.find_all('td', class_="positive")
    negativeChangeList = elements.find_all('td', class_="negative")
    thisDict.update({
        stockSymbol.text: {
            # "Company Name": stockTitle.text,
            "positive" : getStockChange(positiveChangeList),
            "negative" : getStockChange(negativeChangeList)
        }})

print(thisDict)
