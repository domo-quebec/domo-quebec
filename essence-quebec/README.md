# Régie Essence Québec

Extraction et analyse du prix moyen de l'essence par région au Québec.

Source: [https://regieessencequebec.ca/](https://regieessencequebec.ca/)

## Données

Un exemple de données extraites est disponible dans le dossier [donnees](donnees). Les données sont récupérées au format GeoJSON compressé et contiennent les prix des stations-service par région.

### Structure des données

Les données incluent:

- Les stations-service par région du Québec
- Les prix du carburant régulier disponible
- La géolocalisation des stations

## Extraction des données

### Prix moyen pour tout le Québec

```bash
curl -s https://regieessencequebec.ca/stations.geojson.gz |
  gzip -d -c |
  jq -r "[.features[]
    | .properties.Prices[]
    | select(.GasType == \"Régulier\" and .IsAvailable == true)
    | .Price
    | sub(\"¢\"; \"\")
    | tonumber] | add / length"
```

### Prix moyen pour une région spécifique (ex: Montréal)

```bash
curl -s https://regieessencequebec.ca/stations.geojson.gz |
  gzip -d -c |
  jq -r "[.features[]
    | select(.properties.Region == \"Montréal\")
    | .properties.Prices[]
    | select(.GasType == \"Régulier\" and .IsAvailable == true)
    | .Price
    | sub(\"¢\"; \"\")
    | tonumber] | add / length"
```

## Scripts

### Script Python - Extraction des prix

Le script [essence_extractor.py](scripts/essence_extractor.py) automatise l'extraction des données:

```bash
python scripts/essence_extractor.py
```

**Options:**

- `--region REGION`: Région pour laquelle extraire les prix (ex: Montréal, Capitale-Nationale, etc.)
- `--station STATION`: Nom de la station-service pour extraire les prix spécifiquement
- `--gas-type TYPE`: Type de carburant à extraire (défaut: Régulier)
  - Types disponibles: Régulier, Diesel, Super
- `--output FILE`: Exporte les résultats en JSON
- `--verbose`: Mode détaillé avec affichage des informations d'extraction
- `--list-regions`: Liste toutes les régions administratives disponibles
- `--list-stations`: Liste toutes les stations-services (optionnel: `--region` pour filtrer)
- `--list-gas-types`: Liste tous les types de carburants disponibles

**Exemples:**

```bash
# Prix moyen pour tout le Québec
python scripts/essence_extractor.py

# Prix moyen pour la Capitale-Nationale (carburant régulier par défaut)
python scripts/essence_extractor.py --region "Capitale-Nationale"

# Prix moyen du Diesel à Montréal
python scripts/essence_extractor.py --region "Montréal" --gas-type "Diesel"

# Prix pour une station spécifique
python scripts/essence_extractor.py --region "Montréal" --station "nom_station"

# Exporter en JSON
python scripts/essence_extractor.py --region "Capitale-Nationale" --output result.json

# Lister les régions disponibles
python scripts/essence_extractor.py --list-regions

# Lister les stations à Montréal
python scripts/essence_extractor.py --list-stations --region "Montréal"

# Lister les types de carburants disponibles
python scripts/essence_extractor.py --list-gas-types

# Mode détaillé
python scripts/essence_extractor.py --region "Montréal" --verbose
```

## Régions disponibles

Les régions actuellement disponibles dans la source de données incluent:

- Abitibi-Témiscamingue
- Bas-Saint-Laurent
- Capitale-Nationale
- Centre-du-Québec
- Chaudière-Appalaches
- Côte-Nord
- Estrie
- Gaspésie-Îles-de-la-Madeleine
- Lanaudière
- Laurentides
- Laval
- Mauricie
- Montréal
- Montérégie
- Municipalités hors MRC \ CMM
- Nord-du-Québec
- Outaouais
- Saguenay-Lac-Saint-Jean

## Types de carburants disponibles

- **Régulier** (essence ordinaire) - défaut
- **Diesel**
- **Super** (essence premium)

## Notes

- Les prix sont exprimés en cents (¢) par litre
- Par défaut, seuls les prix de l'essence régulière disponible sont inclus dans les calculs
- Les données sont mises à jour régulièrement sur le site de [Régie Essence Québec](https://regieessencequebec.ca/)
- Utilisez `--list-regions`, `--list-stations`, et `--list-gas-types` pour découvrir les options disponibles

## Crédits

Ce répertoire a été développé avec l'aide de Claude Haiku.
