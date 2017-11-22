import urllib
from bs4 import BeautifulSoup

url = 'http://dailytao.org'
html_data = urllib.urlopen(url).read()
soup = BeautifulSoup(html_data,"lxml")
result = soup.find_all('div', attrs={'class':'dailytao'})
for element in result:
    date = element.find('h2')
    tao = element.find('p')
    fineprint = element.find('div', attrs={'class':'fineprint'})
    print('\n\nDaily Tao for ' + date.text)
    print(tao.text + '\n')
