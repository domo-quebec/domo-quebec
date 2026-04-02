# Régie de l'Essence Québec

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

- `--region REGION`: Extrait les prix pour une région spécifique (ex: Montréal, Capitale-Nationale, Outaouais, etc.)
- `--output FILE`: Exporte les résultats en JSON
- `--verbose`: Mode détaillé avec affichage des informations d'extraction

**Exemples:**

```bash
# Prix moyen pour tout le Québec
python scripts/essence_extractor.py

# Prix moyen pour la Capitale-Nationale
python scripts/essence_extractor.py --region "Capitale-Nationale"

# Export en JSON
python scripts/essence_extractor.py --region "Capitale-Nationale" --output result.json

# Mode détaillé
python scripts/essence_extractor.py --verbose
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

## Notes

- Les prix sont exprimés en cents (¢) par litre
- Seuls les prix du carburant régulier disponible sont inclus dans les calculs
- Les données sont mises à jour régulièrement sur le site de la Régie de l'Essence Québec

## Crédits

Ce répertoire a été développé avec l'aide de Claude Haiku.
