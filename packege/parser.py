import requests
from bs4 import BeautifulSoup

def parse_fortnite(name):
    URL='https://fortnitetracker.com/profile/all/'+name
    HEADERS= {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }
    response= requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    stats = soup.findAll('div', class_ = 'trn-card__content')
    comps = []

    for stat in stats:
        comps.append({
        })
#        for comp in comps:
 #           print(comp)
    return "sdsd"


