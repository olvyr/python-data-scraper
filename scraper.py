import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item')
    return [item.text for item in items]

if __name__ == '__main__':
    print('Starting scraper...')
    html = fetch_page('http://example.com')
    if html:
        data = parse_html(html)
        print(f'Found {len(data)} items')