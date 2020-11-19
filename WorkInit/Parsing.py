import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.tenders.kg/'
# /html/body/div[4]/div[3]/div[1]/table/tbody/tr[3]/td[2]/strong[1]/font/span/a

def get_html():
    responce = requests.get(url)
    return responce.text

all_pages = []
all_tenders = []
html = get_html()
soup = BS(html, 'html.parser')

pagination = 'Announcements_list.php?goto='

def get_all_tenders(url):
    link = get_html()
    span = soup.find('tbody').find_all('span')

    for tender in span:
        try:
            a = tender.find('a').get('href')
            a = f"https://www.tenders.kg/{a}"
            all_tenders.append(a)
            print(a)
        except Exception as ex:
            pass

    with open('all_tenders.txt', 'w') as file:
        for tender in all_tenders:
            file.write(f"{tender}\n")

def get_all_pages():
    for page in range(0,106):
        page += 1
        page_url = f'{url}{pagination}{page}'
        all_pages.append(page_url)
        with open("all_pages.txt","w") as file:
            for page in all_pages:
                file.write(f"{page}\n")

get_all_pages()