from bs4 import BeautifulSoup
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

def main():
    url = 'http://dailytao.org'
    html_data = urlopen(url).read()
    soup = BeautifulSoup(html_data,"lxml")
    result = soup.find_all('div', attrs={'class':'dailytao'})
    for element in result:
        date = element.find('h2')
        tao = element.find('p')
        fineprint = element.find('div', attrs={'class':'fineprint'})
        print('\n\nDaily Tao for ' + date.text)
        print(tao.text + '\n')
