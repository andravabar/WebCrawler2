import requests
from bs4 import BeautifulSoup

URL = "https://fp.lhv.ee/market/balticView?locale=et"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("table", class_="data")

# positive = results.find_all('td')
# print(positive)
# print(results)
# for element in elements:
#     print(element)
thisList = []

for element in results:
    symbolList = element.find("a", class_="stock-symbol")
    thisList.append(element)
    # thisDict.update({})
    # positiveChangeList = element.find_all('td', class_="positive")
    # for value in positiveChangeList:
    #     print(value.text.strip())
    # print(positive.text.strip())
    # print()
    # for symbols in symbolList:
    #     print(symbols.text)
    # print(compName.text)

# print(results)

#print(thisList[1])
