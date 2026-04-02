#!/usr/bin/env python3
"""
Script d'extraction du prix moyen de l'essence par région au Québec.
Source: https://regieessencequebec.ca/

Usage:
    python essence_extractor.py                          # Prix moyen du Québec
    python essence_extractor.py --region "Montréal"      # Prix pour une région
    python essence_extractor.py --output result.json     # Export en JSON
"""

import json
import subprocess
import argparse
import sys
from typing import Optional, Dict, List


def get_essence_data(region: Optional[str] = None) -> Optional[Dict]:
    """
    Récupère les données GeoJSON compressées et extrait les prix d'essence.

    Args:
        region: Région optionnelle pour filtrer les résultats

    Returns:
        Dict contenant les statistiques de prix ou None en cas d'erreur
    """
    try:
        # Construction de la requête jq
        if region:
            jq_filter = f"""[.features[]
              | select(.properties.Region == "{region}")
              | .properties.Prices[]
              | select(.GasType == "Régulier" and .IsAvailable == true)
              | .Price
              | sub("¢"; "")
              | tonumber] | {{
                "region": "{region}",
                "count": length,
                "average": (add / length),
                "min": min,
                "max": max
              }}"""
        else:
            jq_filter = """[.features[]
              | .properties.Prices[]
              | select(.GasType == "Régulier" and .IsAvailable == true)
              | .Price
              | sub("¢"; "")
              | tonumber] | {
                "region": "Québec (complet)",
                "count": length,
                "average": (add / length),
                "min": min,
                "max": max
              }"""

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
        result = subprocess.run(
            full_cmd, shell=True, capture_output=True, text=True, timeout=30
        )

        if result.returncode != 0:
            return None

        regions = json.loads(result.stdout)
        return regions

    except Exception as e:
        print(f"Erreur lors de la récupération des régions: {e}", file=sys.stderr)
        return None


def main():
    """Fonction principale."""
    parser = argparse.ArgumentParser(
        description="Extraction du prix moyen de l'essence par région au Québec",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  %(prog)s                              # Prix moyen du Québec
  %(prog)s --region "Montréal"          # Prix pour Montréal
  %(prog)s --output result.json         # Export en JSON
  %(prog)s --list-regions               # Liste les régions disponibles
        """,
    )

    parser.add_argument(
        "--region", type=str, help="Région pour laquelle extraire les prix"
    )
    parser.add_argument("--output", type=str, help="Fichier de sortie JSON (optionnel)")
    parser.add_argument("--verbose", action="store_true", help="Mode détaillé")
    parser.add_argument(
        "--list-regions",
        action="store_true",
        help="Liste toutes les régions disponibles",
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

    # Extraction des données
    if args.verbose:
        if args.region:
            print(f"Extraction des prix pour la région: {args.region}")
        else:
            print("Extraction des prix pour tout le Québec...")

    data = get_essence_data(args.region)

    if data is None:
        sys.exit(1)

    # Affichage des résultats
    if args.verbose:
        print(f"\n{'='*60}")
        print(f"Résion: {data['region']}")
        print(f"{'='*60}")
        print(f"Nombre de prix: {data['count']}")
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
