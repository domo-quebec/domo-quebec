# Nom de la source de donnée

Suivi hydrologique de différentes stations hydrométriques

## Données

Trouvez votre numéro de station sur ce siteweb: https://www.cehq.gouv.qc.ca/suivihydro/

Example : https://www.cehq.gouv.qc.ca/suivihydro/graphique.asp?NoStation=043108
Numéro: 043108

## Installation

### Dépendances

On doit installer l'intégration HACS et HA Multiscrape

### Home-Assistant

Les configurations Home-Assistant du projet Domo-Québec s'installent sous forme de ["package" Home-Assistant](https://www.home-assistant.io/docs/configuration/packages/). Pour faire l'activation de la fonctionnalitée créé un dossier nommé "packages" à la racine de votre dossier de configuratio Home-Assistant et ajoutez la configuration suivante à votre fichier `configuration.yaml`

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Le dossier [home-assistant/packages](home-assistant/packages) contient un fichier nommé `cehq_suivi_hydro.yaml` qui doit être déplacé dans le dossier "packages" de votre installation Home-Assistant.


#### Configuration

Faites un "Rechercher et remplacer" dans le fichier `cehq_suivi_hydro.yaml` et remplacez les valeurs identifiées au début du fichier par les valeurs correspondantes

### Autres plateforme

Si vous utilisez une autre plate-forme qu'Home-Assistant et vous intégrez ces données ce serai grandement apprécié que vous partagiez vos configurations pour les ajouter.

Pour ajouté une plateforme créé un dossier avec le nom de la plateforme à la racine et ajoutez les informations de configuration spécifiques.

