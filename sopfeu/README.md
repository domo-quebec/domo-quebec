# SOPFEU

La [SOPFEU](https://sopfeu.qc.ca) est un organisme de prévention des incendies qui offre un indice du danger d'incendie ainsi que les recommandation correspondantes à chaque niveau.
|Valeur|Niveau|Description|
|-|-|-|
|1|BAS|Risque d’incendie de faible intensité à propagation limitée, c’est le bon moment pour allumer votre feu de camp.|
|2|MODÉRÉ|Risque d’incendie de surface se propageant de façon modérée et se contrôlant généralement bien, faites uniquement des feux de petite dimension (1m X 1m maximum).|
|3|ÉLEVÉ|Risque d’incendie de surface d’intensité modérée à vigoureuse qui pose des défis de contrôle lors du combat terrestre, n’allumez pas si la vitesse du vent est supérieure à 20 km/h.|
|4|TRÈS ÉLEVÉ|Risque d’incendie de forte intensité avec allumage partiel ou complet des cimes dont les conditions au front sont au-delà de la capacité des équipes terrestres, faites des feux seulement dans des installations munies d’un pare-étincelles réglementaire.|
|5|EXTRÊME|Risque d’incendie de cimes de fortes intensité, qui se propage à grande vitesse et qui peut devenir incontrôlable, évitez de faire des feux.|

Source: [https://sopfeu.qc.ca/comment-calcule-t-on-le-danger-dincendie/](https://sopfeu.qc.ca/comment-calcule-t-on-le-danger-dincendie/)

## Installation

### Capteurs

Les valeurs du fichier [sensors.yaml](sensors.yaml) doivent être ajouté à votre configuration. Prenez soin d'ajuster les valeurs "unique_id" et "... --form media=16" afin de refléter la région pour laquelle vous voulez les niveau d'alertes.

**SVP ne réduisez pas inutilement le scan_interval, une vérification à l'heures est amplement suffisante et évite de faire des requête inutiles aux serveurs de SOPFEU.**

### Interface lovelace

Sous le dossier lovelace vous trouverez deux visualisation à ajouter à votre configuration.

#### Jauge

![Jauge SOPFEU](lovelace/jauge/sopfeu-gauge.png)

#### Visuel Forêt


[<img src="lovelace/visuel-foret/foret1.jpeg" width="500"/>](lovelace/visuel-foret/foret1.jpeg)

[<img src="lovelace/visuel-foret/foret2.jpeg" width="500"/>](lovelace/visuel-foret/foret2.jpeg)

## Liste de valeur "media" (Région SOPFEU)

| Media | Emplacement                |
|-------|----------------------------|
| 48    | Baie-des-Chaleurs         |
| 23    | Beauce-Appalaches         |
| 64    | Caniapiscau               |
| 22    | Centre-du-Québec          |
| 29    | Charlevoix                |
| 36    | Chibougamau-Rte du Nord   |
| 53    | Chisasibi                 |
| 38    | Chute-des-Passes          |
| 51    | Eastmain                  |
| 21    | Estrie                    |
| 65    | Fermont-Schefferville     |
| 40    | Forestville-Labrieville    |
| 49    | Gaspé                     |
| 15    | Gatineau                  |
| 60    | Île d'Anticosti            |
| 61    | Îles de la Madeleine       |
| 45    | Kamouraska-RDL-Témisc.    |
| 2     | La Sarre-Amos              |
| 26    | La Tuque                  |
| 37    | Lac Albanel               |
| 32    | Lac-Saint-Jean            |
| 59    | Laforge - 2               |
| 16    | Laurentides               |
| 69    | Le Golfe-du-St-Laurent     |
| 57    | LG-3                       |
| 58    | LG-4                       |
| 8     | Maganasipi-Dumoine         |
| 14    | Manawan                   |
| 43    | Manic 5 - nord SM3        |
| 24    | Maskinongé-Les Chenaux     |
| 1     | Matagami                   |
| 47    | Matane-Chic-Chocs          |
| 6     | Mégiscane-Gouin            |
| 44    | Minganie                  |
| 20    | Montérégie                |
| 63    | Monts-Otish                |
| 35    | Monts-Valin               |
| 54    | Némaska                   |
| 17    | Nord de Montréal          |
| 13    | Outaouais-Labelle          |
| 11    | Parent-Windigo             |
| 12    | Pontiac                   |
| 27    | Portneuf                  |
| 28    | Québec                    |
| 3     | Quévillon-Waswanipi        |
| 56    | Radisson                  |
| 33    | Réserve Ashuapmushuan     |
| 30    | Réserve des Laurentides    |
| 10    | Réserve La Vérendrye       |
| 46    | Rimouski-Matapédia         |
| 68    | Rivière du petit Méticana |
| 34    | Rivière Mistassini         |
| 66    | Rivière Moisie             |
| 67    | Rivière Romaine            |
| 4     | Rouyn-Noranda             |
| 31    | Saguenay                  |
| 55    | Sarcelle                  |
| 42    | Sept-îles                 |
| 25    | St-Maurice-Mastigouche    |
| 7     | Témiscamingue              |
| 62    | Tichégami                 |
| 5     | Val-d'Or-Senneterre        |
| 50    | Waskaganish |
| 52 | Wemindji |
