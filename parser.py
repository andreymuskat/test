import requests
from bs4 import BeautifulSoup as BS

cite = 'https://www.cbr.ru/currency_base/daily/'

full_page = requests.get(cite)

soup = BS(full_page.content, 'html.parser')

content = soup.findAll("tr")

f = open(r"C:\Users\User\Desktop\Курс.txt", "w")

i=0
while i<34:
    i=i+1
    f = open(r"C:\Users\User\Desktop\Курс.txt", "a")
    f.write(content[i].text + '\n' + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' + '\n')
    f.close()
    print(content[i].text)
