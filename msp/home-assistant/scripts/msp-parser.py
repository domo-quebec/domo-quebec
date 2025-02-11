import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def parse_description(description):
    soup = BeautifulSoup(description, 'html.parser')
    data_dict = {}
    for b_tag in soup.find_all('b'):
        key = b_tag.text.strip()
        # Remove leading ': ' from the value
        value = b_tag.next_sibling.strip()
        if value.startswith(": "):
            value = value[2:].strip()
        data_dict[key] = value
    return data_dict

def fetch_rss_feed(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')

    # Get the publication date of the feed and convert to ISO 8601 format
    pub_date = soup.find('pubDate').text
    pub_date_iso = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %z').isoformat()

    items = soup.findAll('item')
    alerts = []
    for item in items:
        title = item.title.text
        description = parse_description(item.description.text)
        alerts.append({
            'title': title,
            'description': description
        })
    return {'publication_date': pub_date_iso, 'alerts': alerts}

url = "https://geoegl.msp.gouv.qc.ca/avp/rss/"
data = fetch_rss_feed(url)
json_data = json.dumps(data, ensure_ascii=False, indent=4)

print(json_data)
