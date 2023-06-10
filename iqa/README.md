# Indice de la qualité de l'air

Une option visuelle der l'indice de la qualité de l'air.

## Installation

- Installer [Swiss Army Knife](https://swiss-army-knife-card-manual.amoebelabs.com/start/installation/).
- Ajouter les sensors.
  - Dans les sensors, changer le site pour celui qui correspond à votre région.
  - Pour trouver votre site, allez sur la page suivante. https://www.iqa.environnement.gouv.qc.ca/contenu/index.asp#
  - Cliquez sur votre région.
  - Cliquez sur "Pour obtenir un historique récent des composantes de l'IQA".
  - Votre site est indiqué dans l'adresse web de la page. 
    - Exemple: https://www.iqa.environnement.gouv.qc.ca/contenu/graph.asp?site=1803
    - 1803 dans mon cas
- Copier le template dans le répertoire /config/lovelace/sak_templates/templates/layouts/
- Copier les images dans le répertoire /config/www/mes_images/
- Copier iqa.yaml
- Redémarrer Home Assistant

### Captures d'écran

![image](https://github.com/MichelJourdain/domo-quebec/assets/83040228/389b4a72-d5eb-402a-af15-41df2f593f52)

![image](https://github.com/MichelJourdain/domo-quebec/assets/83040228/974c46be-c8e6-4ee0-ab52-f4e8d286800c)

![image](https://github.com/MichelJourdain/domo-quebec/assets/83040228/c5344fff-0b5e-44f2-8eba-c968e1f7185c)

Crédit : [https://github.com/MichelJourdain/](https://github.com/MichelJourdain/)
