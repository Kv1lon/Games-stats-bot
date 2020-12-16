import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def send_message(comps):
    text= ""
    for comp in comps:
        if comp['title'] and comp['value']:
            text += comp['title'] +" : " + comp['value']+"\n"
    return text

def fortnite(name, bot, message):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.get('https://fortnitetracker.com/profile/all/' + name)
    generated_html = browser.page_source
    browser.quit()
    soup = BeautifulSoup(generated_html, 'html.parser')
    items_solo = soup.find('div', class_='trn-card trn-card--ftr-blue').find('div', class_='trn-defstats').find_all('div', class_='trn-defstat')
    items_duos = soup.find('div', class_='trn-card trn-card--ftr-green').find('div', class_='trn-defstats').find_all('div', class_='trn-defstat')
    items_squads = soup.find('div', class_='trn-card trn-card--ftr-purple').find('div', class_='trn-defstats').find_all('div', class_='trn-defstat')
    matches_count_solo = soup.find('div', class_='trn-card trn-card--ftr-blue').find('span', class_='trn-card__header-subline').get_text(strip=True).replace("Матчи", "")
    matches_count_duos = soup.find('div', class_='trn-card trn-card--ftr-green').find('span', class_='trn-card__header-subline').get_text(strip=True).replace("Матчи", "")
    matches_count_squads = soup.find('div', class_='trn-card trn-card--ftr-purple').find('span', class_='trn-card__header-subline').get_text(strip=True).replace("Матчи", "")
    comps_solo = []
    comps_duos = []
    comps_squads = []

    for item in items_solo:
        comps_solo.append(
                {
                    'title': item.find('div', class_='trn-defstat__name').get_text(strip=True),
                    'value': item.find('div', class_='trn-defstat__values').get_text(strip=True),

                }
            )
    for item in items_duos:
        comps_duos.append(
            {
                'title': item.find('div', class_='trn-defstat__name').get_text(strip=True),
                'value': item.find('div', class_='trn-defstat__values').get_text(strip=True),

            }
        )
    for item in items_squads:
        comps_squads.append(
            {
                'title': item.find('div', class_='trn-defstat__name').get_text(strip=True),
                'value': item.find('div', class_='trn-defstat__values').get_text(strip=True),

            }
        )
    bot.send_message(message.chat.id, f"Solo:\nmatches: {matches_count_solo}")
    bot.send_message(message.chat.id, send_message(comps_solo))
    bot.send_message(message.chat.id, f"Duos:\nmatches: {matches_count_duos}")
    bot.send_message(message.chat.id, send_message(comps_duos))
    bot.send_message(message.chat.id, f"Squads:\nmatches:{matches_count_squads} ")
    bot.send_message(message.chat.id, send_message(comps_squads))


