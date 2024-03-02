# CAA

## Données
Le CAA publie le prix de l'essence par région sur son site [https://www.caa.ca/fr/prix-de-lessence/](https://www.caa.ca/fr/prix-de-lessence/)

Il est possible d'extraire ces données en format json avec la commande suivante: `curl -s --request POST "https://www.caa.ca/wp/wp-admin/admin-ajax.php" --form action=getCitiesForDropdown --form caa_dropdown=QUEBEC`

## Installation

### Home-Assistant

Les configurations Home-Assistant du projet Domo-Québec s'installent sous forme de ["package" Home-Assistant](https://www.home-assistant.io/docs/configuration/packages/). Pour faire l'activation de la fonctionnalitée créé un dossier nommé "packages" à la racine de votre dossier de configuratio Home-Assistant et ajoutez la configuration suivante à votre fichier `configuration.yaml`

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Le dossier [home-assistant/packages](home-assistant/packages) contient un fichier nommé `caa.yaml` qui doit être déplacé dans le dossier "packages" de votre installation Home-Assistant.

#### Configuration

Dans le fichier `caa.yaml`, remplacer `VILLE` par votre ville disponible dans le tableau ci-bas.


| Ville disponibles|
|-------|
| MONTREAL |
| ALMA |
| BLAINVILLE |
| BROSSARD |
| CHICOUTIMI |
| DRUMMONDVILLE |
| GASPE |
| GATINEAU |
| GRANBY |
| LAVAL |
| LEVIS |
| LONGUEUIL |
| MAGOG |
| MATANE |
| QUEBEC |
| REPENTIGNY |
| RIMOUSKI |
| RIVIERE-DU-LOUP |
| ROUYN-NORANDA |
| SAINT-EUSTACHE |
| SAINT-HYACINTHE |
| SAINT-JEAN-SUR-RICHELIEU |
| SAINT-JEROME |
| SEPT-ILES |
| SHAWINIGAN |
| SHERBROOKE |
| TROIS-RIVIERES |
| VAL-D'OR |
| VAUDREUIL-DORION |

#### Cartes Lovelace
Un exemple de carte lovelace est disponible dans le dossier [home-assistant/lovelaces](home-assistant/lovelaces)


## TODO

- Ajouter Bruno