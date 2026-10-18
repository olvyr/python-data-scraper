import requests
import pandas as pd
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

def export_to_csv(data, filename):
    df = pd.DataFrame(data, columns=['ItemName'])
    df.to_csv(filename, index=False)
    print(f'Exported to {filename}')

if __name__ == '__main__':
    print('Starting scraper...')
    html = fetch_page('http://example.com')
    if html:
        data = parse_html(html)
        export_to_csv(data, 'output.csv')