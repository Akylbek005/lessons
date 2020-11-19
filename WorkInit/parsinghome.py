import requests
from bs4 import BeautifulSoup as BS

url  = 'https://www.mozaweb.kg/en/MyLearn/homework'

def get_html ():
    response = requests.get(url)
    return  response.text

all_name = []


html = get_html()
soup = BS(html, 'html.parser')

def get_all_name():
    table  = soup.find('table')
    if table in soup:
        a = table.find('tr').get('p')
        all_name.append(a)
        print(all_name)

    with open('all_name.txt', 'w') as file:
        for i in all_name:
            file.write(f'{i}\n')

get_all_name()

