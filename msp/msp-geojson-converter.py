import requests
import json
from pyproj import Transformer

url = "https://geoegl.msp.gouv.qc.ca/ws/igo_gouvouvert.fcgi?service=wfs&version=1.1.0&request=getfeature&typename=msp_vigilance_crue_publique_v_type&outputformat=geojson"

# Fetch the geojson file
response = requests.get(url)
data = response.json()

# Define the coordinate transformation
transformer = Transformer.from_crs("EPSG:32198", "EPSG:4326")

# Convert the coordinates for each feature
for feature in data['features']:
    geometry = feature['geometry']
    # Convert coordinates
    geometry['coordinates'] = transformer.transform(*geometry['coordinates'])

# Preserve accented characters in properties
data_str = json.dumps(data, ensure_ascii=False).encode('cp1252').decode('utf-8')

# Save the converted geojson to a file
with open('www/msp.geojson', 'w', encoding='utf-8') as file:
    file.write(data_str)
#print(json.dumps(data_str, indent=4,ensure_ascii=False))
