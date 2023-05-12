import requests
from bs4 import BeautifulSoup
import json

def parse_description(description):
    soup = BeautifulSoup(description, 'html.parser')
    data_dict = {}
    for b_tag in soup.find_all('b'):
        key = b_tag.text.strip()
        value = b_tag.next_sibling.strip()
        data_dict[key] = value
    return data_dict

def fetch_rss_feed(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')

    items = soup.findAll('item')
    data = []
    for item in items:
        title = item.title.text
        description = parse_description(item.description.text)
        data.append({
            'title': title,
            'description': description
        })
    return data

url = "https://geoegl.msp.gouv.qc.ca/avp/rss/"
data = fetch_rss_feed(url)
json_data = json.dumps(data, ensure_ascii=False, indent=4)

print(json_data)
