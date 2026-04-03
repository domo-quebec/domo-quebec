#!/usr/bin/env python3
"""
Script d'extraction du prix moyen de l'essence par région au Québec.
Source: https://regieessencequebec.ca/

Usage:
    python essence_extractor.py                                  # Prix moyen du Québec
    python essence_extractor.py --region "Montréal"              # Prix pour une région
    python essence_extractor.py --region "Montréal" --gas-type "Diesel"  # Type de carburant spécifique
    python essence_extractor.py --station "nom" --region "montréal"  # Prix pour une station
    python essence_extractor.py --output result.json             # Export en JSON
    python essence_extractor.py --list-regions                   # Liste les régions
    python essence_extractor.py --list-gas-types                 # Liste les types de carburants
"""

import json
import subprocess
import argparse
import sys
from typing import Optional, Dict, List


def get_essence_data(
    region: Optional[str] = None,
    station: Optional[str] = None,
    gas_type: str = "Régulier",
) -> Optional[Dict]:
    """
    Récupère les données GeoJSON compressées et extrait les prix d'essence.

    Args:
        region: Région optionnelle pour filtrer les résultats
        station: Nom de la station spécifique (optionnel)
        gas_type: Type de carburant (défaut: Régulier)

    Returns:
        Dict contenant les statistiques de prix ou None en cas d'erreur
    """
    try:
        # Construction de la requête jq
        filters = f'.GasType == "{gas_type}" and .IsAvailable == true'

        if station and region:
            jq_filter = f"""[.features[]
              | select(.properties.Region == "{region}")
              | select(.properties.Name == "{station}")
              | .properties.Prices[]
              | select({filters})
              | .Price
              | sub("¢"; "")
              | tonumber] | {{
                "region": "{region}",
                "station": "{station}",
                "gas_type": "{gas_type}",
                "count": length,
                "average": (add / length),
                "min": min,
                "max": max
              }}"""
        elif station:
            jq_filter = f"""[.features[]
              | select(.properties.Name == "{station}")
              | .properties.Prices[]
              | select({filters})
              | .Price
              | sub("¢"; "")
              | tonumber] | {{
                "station": "{station}",
                "gas_type": "{gas_type}",
                "count": length,
                "average": (add / length),
                "min": min,
                "max": max
              }}"""
        elif region:
            jq_filter = f"""[.features[]
              | select(.properties.Region == "{region}")
              | .properties.Prices[]
              | select({filters})
              | .Price
              | sub("¢"; "")
              | tonumber] | {{
                "region": "{region}",
                "gas_type": "{gas_type}",
                "count": length,
                "average": (add / length),
                "min": min,
                "max": max
              }}"""
        else:
            jq_filter = f"""[.features[]
              | .properties.Prices[]
              | select({filters})
              | .Price
              | sub("¢"; "")
              | tonumber] | {{
                "region": "Québec (complet)",
                "gas_type": "{gas_type}",
                "count": length,
                "average": (add / length),
                "min": min,
                "max": max
              }}"""

        # Exécution de la commande avec un pipeline pour éviter les problèmes avec les guillemets
        try:
            curl_proc = subprocess.Popen(
                ["curl", "-s", "https://regieessencequebec.ca/stations.geojson.gz"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            gzip_proc = subprocess.Popen(
                ["gzip", "-d", "-c"],
                stdin=curl_proc.stdout,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            curl_proc.stdout.close()

            jq_proc = subprocess.Popen(
                ["jq", "-r", jq_filter],
                stdin=gzip_proc.stdout,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            gzip_proc.stdout.close()

            stdout, stderr = jq_proc.communicate(timeout=30)

            if jq_proc.returncode != 0:
                print(f"Erreur lors de l'extraction: {stderr}", file=sys.stderr)
                return None

            # Parse le résultat JSON
            data = json.loads(stdout)
            return data

        except subprocess.TimeoutExpired:
            print("Erreur: La requête a expirée (timeout)", file=sys.stderr)
            return None
    except json.JSONDecodeError as e:
        print(f"Erreur: Impossible de parser les données JSON: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Erreur: {e}", file=sys.stderr)
        return None


def get_all_regions() -> Optional[List[str]]:
    """
    Récupère la liste de toutes les régions disponibles.

    Returns:
        Liste des régions disponibles ou None en cas d'erreur
    """
    try:
        curl_cmd = "curl -s https://regieessencequebec.ca/stations.geojson.gz"
        jq_filter = "[.features[].properties.Region] | unique | sort"

        full_cmd = f"{curl_cmd} | gzip -d -c | jq -r '{jq_filter}'"
        result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True, timeout=30)

        if result.returncode != 0:
            return None

        regions = json.loads(result.stdout)
        return regions

    except Exception as e:
        print(f"Erreur lors de la récupération des régions: {e}", file=sys.stderr)
        return None


def get_all_stations(region: Optional[str] = None) -> Optional[List[str]]:
    """
    Récupère la liste de toutes les stations-services disponibles.

    Args:
        region: Région optionnelle pour filtrer

    Returns:
        Liste des stations disponibles ou None en cas d'erreur
    """
    try:
        curl_cmd = "curl -s https://regieessencequebec.ca/stations.geojson.gz"
        if region:
            jq_filter = f'[.features[] | select(.properties.Region == "{region}") | .properties.Name] | unique | sort'
        else:
            jq_filter = "[.features[].properties.Name] | unique | sort"

        full_cmd = f"{curl_cmd} | gzip -d -c | jq -r '{jq_filter}'"
        result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True, timeout=30)

        if result.returncode != 0:
            return None

        stations = json.loads(result.stdout)
        return stations

    except Exception as e:
        print(f"Erreur lors de la récupération des stations: {e}", file=sys.stderr)
        return None


def get_all_gas_types() -> Optional[List[str]]:
    """
    Récupère la liste de tous les types de carburants disponibles.

    Returns:
        Liste des types de carburants disponibles ou None en cas d'erreur
    """
    try:
        curl_cmd = "curl -s https://regieessencequebec.ca/stations.geojson.gz"
        jq_filter = "[.features[].properties.Prices[].GasType] | unique | sort"

        full_cmd = f"{curl_cmd} | gzip -d -c | jq -r '{jq_filter}'"
        result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True, timeout=30)

        if result.returncode != 0:
            return None

        gas_types = json.loads(result.stdout)
        return gas_types

    except Exception as e:
        print(f"Erreur lors de la récupération des types de carburants: {e}", file=sys.stderr)
        return None


def main():
    """Fonction principale."""
    parser = argparse.ArgumentParser(
        description="Extraction du prix moyen de l'essence par région au Québec",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  %(prog)s                                              # Prix moyen du Québec
  %(prog)s --region "Montréal"                          # Prix pour Montréal
  %(prog)s --region "Montréal" --gas-type "Diesel"      # Prix du Diesel à Montréal
  %(prog)s --station "name" --region "Montréal"         # Prix pour une station spécifique
  %(prog)s --output result.json                         # Export en JSON
  %(prog)s --list-regions                               # Liste les régions
  %(prog)s --list-stations --region "Montréal"          # Liste les stations de Montréal
  %(prog)s --list-gas-types                             # Liste les types de carburants
        """,
    )

    parser.add_argument("--region", type=str, help="Région pour laquelle extraire les prix")
    parser.add_argument(
        "--station",
        type=str,
        help="Nom de la station-service pour laquelle extraire les prix",
    )
    parser.add_argument(
        "--gas-type",
        type=str,
        default="Régulier",
        help="Type de carburant (défaut: Régulier)",
    )
    parser.add_argument("--output", type=str, help="Fichier de sortie JSON (optionnel)")
    parser.add_argument("--verbose", action="store_true", help="Mode détaillé")
    parser.add_argument(
        "--list-regions",
        action="store_true",
        help="Liste toutes les régions disponibles",
    )
    parser.add_argument(
        "--list-stations",
        action="store_true",
        help="Liste les stations-services disponibles (optionnel: --region pour filtrer)",
    )
    parser.add_argument(
        "--list-gas-types",
        action="store_true",
        help="Liste tous les types de carburants disponibles",
    )

    args = parser.parse_args()

    # Liste des régions
    if args.list_regions:
        if args.verbose:
            print("Récupération de la liste des régions...")

        regions = get_all_regions()
        if regions:
            print(f"Régions disponibles ({len(regions)}):\n")
            for region in regions:
                print(f"{region}")
        return

    # Liste des stations
    if args.list_stations:
        if args.verbose:
            if args.region:
                print(f"Récupération des stations de {args.region}...")
            else:
                print("Récupération de toutes les stations...")

        stations = get_all_stations(args.region)
        if stations:
            region_text = f"dans {args.region}" if args.region else "au Québec"
            print(f"Stations disponibles {region_text} ({len(stations)}):\n")
            for station in stations:
                print(f"{station}")
        return

    # Liste des types de carburants
    if args.list_gas_types:
        if args.verbose:
            print("Récupération de la liste des types de carburants...")

        gas_types = get_all_gas_types()
        if gas_types:
            print(f"Types de carburants disponibles ({len(gas_types)}):\n")
            for gas_type in gas_types:
                print(f"{gas_type}")
        return

    # Extraction des données
    if args.verbose:
        if args.station:
            region_text = f"dans {args.region}" if args.region else ""
            print(f"Extraction des prix pour la station {args.station} {region_text}")
        elif args.region:
            print(f"Extraction des prix pour la région: {args.region} ({args.gas_type})")
        else:
            print(f"Extraction des prix pour tout le Québec ({args.gas_type})...")

    data = get_essence_data(args.region, args.station, args.gas_type)

    if data is None:
        sys.exit(1)

    # Affichage des résultats
    if args.verbose:
        print(f"\n{'='*60}")
        if "station" in data:
            print(f"Station: {data.get('station', 'N/A')}")
        if "region" in data:
            print(f"Région: {data.get('region', 'N/A')}")
        print(f"Carburant: {data.get('gas_type', 'N/A')}")
        print(f"{'='*60}")
        print(f"Nombre de prix: {data['count']}")
        if data["count"] > 0:
            print(f"Prix moyen: {data['average']:.2f}¢/L")
            print(f"Prix minimum: {data['min']:.2f}¢/L")
            print(f"Prix maximum: {data['max']:.2f}¢/L")
        print(f"{'='*60}")
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))

    # Export en JSON si demandé
    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            if args.verbose:
                print(f"\nDonnées exportées vers: {args.output}")
        except IOError as e:
            print(f"Erreur lors de l'écriture du fichier: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
