#  Ministère de l’Environnement, de la Lutte contre les changements climatiques, de la Faune et des Parcs

## Indice de la qualité de l’air

Le ministère de l’Environnement, de la Lutte contre les changements climatiques, de la Faune et des Parcs publie les indices de la qualité de l’air sur son site web à cette adresse : [https://www.iqa.environnement.gouv.qc.ca/contenu/index.asp](https://www.iqa.environnement.gouv.qc.ca/contenu/index.asp)

Un capteur permet d’ajouter l’indice de la qualité de l’air à Home-Assistant et est disponible dans le sous-dossier IQA.


## Installation

### Home-Assistant

Les configurations Home-Assistant du projet Domo-Québec s'installent sous forme de ["package" Home-Assistant](https://www.home-assistant.io/docs/configuration/packages/). Pour faire l'activation de la fonctionnalitée créé un dossier nommé "packages" à la racine de votre dossier de configuratio Home-Assistant et ajoutez la configuration suivante à votre fichier `configuration.yaml`

```yaml
homeassistant:
  packages: !include_dir_named packages
```



Le dossier [home-assistant/packages](home-assistant/packages) contient un fichier nommé `melccfp.yaml` qui doit être déplacé dans le dossier "packages" de votre installation Home-Assistant.

#### Configuration

- Adapter la configuration des sensors dans le fichier `melccfp.yaml`:
  - Dans la propriété `resource` du premier sensor, changer le numéro de station pour celui qui correspond à votre région.
    - Pour trouver votre numéro de station, allez sur la page suivante: http://www.arcgis.com/apps/mapviewer/index.html?url=https://services3.arcgis.com/0lL78GhXbg1Po7WO/ArcGIS/rest/services/IQA_resultat_REST/FeatureServer&source=sd
    - Cliquez sur la station voulue
    - Prenez en note la valeur de `NO_STATION`
  - Mettre à jour les valeurs des propriétés `name`, `unique_id` et `friendly_name` des deux sensors selon vos préférences

Pour le lovelace :

- Installer [Swiss Army Knife](https://swiss-army-knife-card-manual.amoebelabs.com/start/installation/).
- Copier le template dans le répertoire /config/lovelace/sak_templates/templates/layouts/
- Copier les images dans le répertoire /config/www/mes_images/
- Copier `melccfp.yaml`
- Mettre à jour les noms des sensors dans `melccfp.yaml` selon votre configuration


### Captures d'écran

![image](https://github.com/MichelJourdain/domo-quebec/assets/83040228/389b4a72-d5eb-402a-af15-41df2f593f52)

![image](https://github.com/MichelJourdain/domo-quebec/assets/83040228/974c46be-c8e6-4ee0-ab52-f4e8d286800c)

![image](https://github.com/MichelJourdain/domo-quebec/assets/83040228/c5344fff-0b5e-44f2-8eba-c968e1f7185c)

Crédit : [https://github.com/MichelJourdain/](https://github.com/MichelJourdain/)
