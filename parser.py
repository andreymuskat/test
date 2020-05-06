import requests
from bs4 import BeautifulSoup as BS

cite = 'https://www.cbr.ru/currency_base/daily/'

full_page = requests.get(cite)

soup = BS(full_page.content, 'html.parser')

content = soup.findAll("tr")

f = open(r"C:\Users\User\Desktop\Курс.txt", "w")
f.close()
i=0
while i<34:
    f = open(r"C:\Users\User\Desktop\Курс.txt", "a")
    f.write(content[i].text + '\n' + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' + '\n')
    f.close()
    print(content[i].text)
    i=i+1
file = open(r"C:\Users\User\Desktop\Курс.txt", "r")
print (file.read())
file.close()
import os
file_delete = "C:/Users/User/Desktop/Курс.txt"
os.remove(file_delete)    
