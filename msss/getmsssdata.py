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
# Step 4a: Remove Apostrophe and parenthesis from the "Heure_de_l'extraction_(image)" header
header_line = header_line.replace("Heure_de_l'extraction_(image)", "Heure_de_lextraction_image")
# Step 4b: Remove trailing space from the "Nombre_de_civieres_fonctionnelles " header
header_line = header_line.replace('Nombre_de_civieres_fonctionnelles ', 'Nombre_de_civieres_fonctionnelles')
lines[0] = header_line

# Read the CSV data
csv_data = csv.reader(lines, delimiter=',')
csv_rows = [row for row in csv_data]

# Step 5: Convert the CSV to JSON
headers = csv_rows[0]
json_data = {}
for row in csv_rows[1:]:
    if len(row) > 0:  # Check if the row is not empty
        rsss = row[0]
        entry = {header: value for header, value in zip(headers[1:], row[1:])}
        if rsss not in json_data:
            json_data[rsss] = []
        json_data[rsss].append(entry)

# Step 6: Save the JSON data
output_file = 'data_msss.json'
with open(output_file, 'w') as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)

# Step 7: Output the JSON data
print(json.dumps(json_data, indent=4, ensure_ascii=False))
