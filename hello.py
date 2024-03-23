import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.bangkokpost.com/life/tech'
r = requests.get(url)
page_html = r.text

data = soup(page_html, 'html.parser')

links = data.find_all('div', {'class':'news--list-text'})

for l in links:
    text = l.h3.text
    text = text.replace('\n','')
    text = text.replace('\t','')
    print(text)
    print('-----')