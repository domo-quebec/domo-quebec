import csv
import json
import requests

# Step 1: Download the CSV file
url = 'https://www.msss.gouv.qc.ca/professionnels/statistiques/documents/urgences/Releve_horaire_urgences_7jours_nbpers.csv'
response = requests.get(url)

# Step 2: Convert character encoding from Windows-1252 to UTF-8
content = response.content.decode('windows-1252').encode('utf-8').decode('utf-8')

# Step 3: Remove extra tabulations
content = content.replace('\t', '')

# Split the content into lines and remove leading space from the " Mise_a_jour" header
lines = content.split('\n')
header_line = lines[0]

# Step 4: Remove leading space from the " Mise_a_jour" header
header_line = header_line.replace(' Mise_a_jour', 'Mise_a_jour')
lines[0] = header_line

# Read the CSV data
csv_data = csv.reader(lines, delimiter=',')
csv_rows = [row for row in csv_data]

# Step 5: Convert the CSV to JSON
headers = csv_rows[0]
json_data = [dict(zip(headers, row)) for row in csv_rows[1:]]

# Step 6: Output the JSON data
print(json.dumps(json_data, indent=4, ensure_ascii=False))
