# Données - Prix de l'Essence Québec

Ce dossier contient des exemples d'extractions de données de la Régie de l'Essence Québec.

## Fichiers

- `exemple_quebec_complet.json`: Exemple de résultat pour tout le Québec
- `exemple_montreal.json`: Exemple de résultat pour la région de Montréal
- `exemple_quebec_ville.json`: Exemple de résultat pour la région de Québec

## Structure des données

Chaque fichier contient:

```json
{
  "region": "Région",
  "count": "Nombre de prix inclus",
  "average": "Prix moyen en cents/litre",
  "min": "Prix minimum en cents/litre",
  "max": "Prix maximum en cents/litre"
}
```

## Mise à jour

Les données sont des exemples statiques utilisés pour le développement et les tests. Pour obtenir les données actuelles, exécuter le script `essence_extractor.py`:

```bash
python ../scripts/essence_extractor.py --verbose
```

## Exemples d'extraction

### Commande cURL directe

Pour extraire le prix moyen de l'essence à Montréal:

```bash
curl -s https://regieessencequebec.ca/stations.geojson.gz |
  gzip -d -c |
  jq -r "[.features[]
    | select(.properties.Region == \"Montréal\")
    | .properties.Prices[]
    | select(.GasType == \"Régulier\" and .IsAvailable == true)
    | .Price
    | sub(\"¢\"; \"\")
    | tonumber] | (add / length * 10 | round) / 10"
```

### Lister les régions disponibles

Pour obtenir la liste des régions administratives pouvant être utilisées:

```bash
curl -s https://regieessencequebec.ca/stations.geojson.gz |
  gzip -d -c |
  jq -r "[.features[].properties.Region] | unique[]"
```

Ou avec le script Python:

```bash
python ../scripts/essence_extractor.py --list-regions
```

### Configuration Home Assistant

Pour intégrer le prix de l'essence à Home Assistant, ajouter la configuration suivante au fichier `configuration.yaml`:

```yaml
command_line:
  - sensor:
      name: "Prix essence moyen Montréal"
      command: >
        bash -c 'curl -s https://regieessencequebec.ca/stations.geojson.gz |
        gzip -d -c |
        jq -r "[.features[]
          | select(.properties.Region == \"Montréal\")
          | .properties.Prices[]
          | select(.GasType == \"Régulier\" and .IsAvailable == true)
          | .Price
          | sub(\"¢\"; \"\")
          | tonumber] | (add / length * 10 | round) / 10"'
      unit_of_measurement: "¢/L"
      scan_interval: 600
```

Cette configuration:

- Récupère le prix moyen toutes les 10 minutes (`scan_interval: 600`)
- Affiche la valeur avec l'unité de mesure correcte (`¢/L`)
- Arrondit la valeur à 1 chiffre décimal
