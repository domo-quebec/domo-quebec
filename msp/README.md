# MSP

**En développement, bienvenu aux contributions**

## Convertisseur RSS vers JSON

Le fichier msp-geojson-parser.py permet d'extraire le [fil RSS Multi-Risque](https://www.donneesquebec.ca/recherche/dataset/carte-vigilance-multirisque-fil
) du Ministère de la sécurité publique et le converti au format json.

## Convertisseur Geojson

Le MSP fourni un fichier Geojson avec des coordonéees aui format ESPG:32198. Le script msp-geojson-converter.py récupère le fichier et le converti au format ESPG:4326 (format GPS) ce qui permet son utilisation dans Home-Assistant avec l'extension GeoJson.



## TODO

- Ajouter des exemples de sensors Home-Assistant
- Ajouter un exemple de carte lovelace
