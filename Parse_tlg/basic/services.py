import requests
from bs4 import BeautifulSoup


def find_song():
    url_our = 'https://top-radio.ru/playlist/avtoradio'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    headers = {
        'user agent': user_agent,
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
    }
    html = requests.get(url_our, headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    name_tracks = soup.findAll('div', {'class': 'name_track'})
    for element in name_tracks:
        artist = element.findAll('span', {'class': 'artist'})
        song = element.findAll('span', {'class': 'song'})
        name = f'Сейчас играет: {artist[0].text} - {song[0].text}'
        return name
