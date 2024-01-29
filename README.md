# Domo Québec

Ce dépôt a pour but de documenter l'accès à différentes ressources d'intérêt pour les Québécois exploitant des systèmes de domotique. La plupart des solutions proposées ont été faites pour la plateforme Home-Assistant, mais les techniques pour l'extraction des données devraient être transposables dans d'autres plates-formes.

## Contribution

Si vous avez des idées d'autres sources de données d'intérêt n'hésitez pas à ouvrir un issue ou faire un pull request.

Veuillez utiliser le dossier [00-modele](/00-modele/) comme base pour la structure de votre intégration.

Les nouvelles sources de données sont ajoutées à ce dépôt git. Lorsque l'intégration est stable et jugée complete elle pourra être déplacée vers un dépôt indépendant.


## Plateformes

| Plateforme | Description | État |
|-|-|-|
| CITAM | [Alertes Municipales](/citam/) | En cours |
| CAA | [Prix Essence](/caa/) | Fonctionnel |
| Hydro-Québec | [Données Ouvertes](/hydro-quebec/) | Fonctionnel |
| MELCCFP | [Indice de la qualité de l'air](/melccfp/) | Fonctionnel |
| MSP | [Fil multirisque](/msp/) | En cours |
| MTQ | [Caméras](/mtq/) | Fonctionnel |

## TODO

- Touver un moyen d'intégrer les données du fil multi-risque du MSP (feu, inondations, alertes météo, etc) [https://www.donneesquebec.ca/recherche/dataset/carte-vigilance-multirisque-fil](https://www.donneesquebec.ca/recherche/dataset/carte-vigilance-multirisque-fil)
- Intégré les données du MTQ sur les travaux routier à proximité
