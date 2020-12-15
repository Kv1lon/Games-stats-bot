import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def parse(name):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)

    browser.get('https://fortnitetracker.com/profile/all/'+name)
# ... other actions
    generated_html = browser.page_source
    browser.quit()
    soup = BeautifulSoup(generated_html, 'html.parser')
    items = soup.findAll('div',class_='trn-card')
    comps = []
    for item in  items:
        comps.append(
            {
                'title': item.find('h2', class_ = 'trn-card__header-title'),
                'wins': item.find('div', class_='trn-defstat__value'),

            }
        )
        for comp in comps:
            return "fdf"
