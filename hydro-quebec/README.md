# Hydro-Québec

Le projet [hydroqc](https://hydroqc.ca) est le meilleur système pour l'intégration de vos données de compte Hydro-Québec à votre plateforme domotique.

Il y a tout de même certaines données plus globales publiées par Hydro-Québec qui peuvent être intéressantes à intégrer à votre système.

## Données

### Demande de puissance du réseau

La demande de puissance du réseau d'Hydro-Québec est disponible à l'adresse suivante et est rafraichie aux 15 min [https://www.hydroquebec.com/data/documents-donnees/donnees-ouvertes/json/demande.json](https://www.hydroquebec.com/data/documents-donnees/donnees-ouvertes/json/demande.json)

![Demande de puissance](images/demande-puissance.png)

Merci riceandpasta#2144 sur le [Discord](https://discord.gg/BTPDntfaXH) du projet [Hydroqc](https://hydroqc.ca) pour la configuration initiale.

### Production électrique

Les données des sources d'électricité d'Hydro-Québec sont disponibles [https://www.hydroquebec.com/data/documents-donnees/donnees-ouvertes/json/production.json](https://www.hydroquebec.com/data/documents-donnees/donnees-ouvertes/json/production.json). Il est important de savoir que les données ont un [décalage](https://www.hydroquebec.com/documents-donnees/donnees-ouvertes/production-electricite-quebec/).

## Autres configurations d'intérêt

Le dossier [hydro-quebec/home-assistant/packages]hydro-quebec/home-assistant/packages contient deux fichiers "tarif" qui sont des configurations qui peuvent être utilisées avec un lecteur de consommation électrique "live" pour calculer le cout de l'électricité consommée.

## Installation

### Home-Assistant

Les configurations Home-Assistant du projet Domo-Québec s'installent sous forme de ["package" Home-Assistant](https://www.home-assistant.io/docs/configuration/packages/). Pour faire l'activation de la fonctionnalité, créez un dossier nommé "packages" à la racine de votre dossier de configuration Home-Assistant et ajoutez la configuration suivante à votre fichier `configuration.yaml`.

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Le dossier [home-assistant/packages](home-assistant/packages) contient des fichiers qui doivent être déplacés dans le dossier "packages" de votre installation Home-Assistant.

#### Configuration

Faites un "Rechercher et remplacer" dans le fichier `fermeture-ecoles.yaml` et remplacer les valeurs identifiées au début du fichier par les valeurs correspondantes.
