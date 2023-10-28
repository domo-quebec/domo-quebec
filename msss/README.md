# MSSS

**En développement, bienvenu aux contributions**

Le ministère de la Santé et des Services sociaux publie plusieurs données.

## État d'occupation des urgences (horaire)

Un fichier CSV est rafraichi à chaque heure environ et est disponible à l'adresse suivante : [https://www.msss.gouv.qc.ca/professionnels/statistiques/documents/urgences/Releve_horaire_urgences_7jours_nbpers.csv](https://www.msss.gouv.qc.ca/professionnels/statistiques/documents/urgences/Releve_horaire_urgences_7jours_nbpers.csv)

Le format CSV se prête mal à l'interprétation des données et ce fichier plus particulièrement comporte plusieurs irrégularités au niveau de caractère superflu. Un petit script python permet de nettoyer les données et les convertir au format json.

## Installation
### Acquisition des donnés
* Le script python [getmsssdata.py](getmsssdata.py) doit etre placé dans vos fichier de configuration Home Assistant.
* Ajouter le contenu du fichier [configuration.yaml](configuration.yaml) dans votre fichier `configuration.yaml` de Home Assistant.
* Remplacer `[VOTRE_URL_HA]` par l'URL de votre serveur Home Assistant.
* Remplacer les numéros d'attributs en vous aidant du tableau si dessous.
* Finalement, créer une automatisation qui vas permettre d'actualisé le fichier source tout les 15 minutes.
```
trigger:
  - platform: time_pattern
    minutes: /15
action:
  - service: shell_command.execute_python_script_msss
    data: {}
```
| Numéro | Région |
|----------|----------|
| 01 | Bas-Saint-Laurent |
| 02 | Saguenay-Lac-Saint-Jean |
| 03 | Capitale-Nationale |
| 04 | Mauricie et Centre-du-Québec |
| 05 | Estrie |
| 06 | Montréal |
| 07 | Outaouais |
| 08 | Abitibi-Témiscamingue |
| 09 | Côte-Nord |
| 11 | Gaspésie-Îles-de-la-Madeleine |
| 12 | Chaudière-Appalaches |
| 13 | Laval |
| 14 | Lanaudière |
| 15 | Laurentides |
| 16 | Montérégie |
| 99 | Ensemble du Québec |

### Capteurs
Deux solutions sont possible pour les capteurs. La [métode 1](methode1/configuration.yaml) est un sensor par région qui contient tout les données en attributs.

La [métode 2](methode2/configuration.yaml) est un sensor différent par donnée.

### Méthode 1
* Ajouter le contenu de fichier [metode1/configuration.yaml](methode1/configuration.yaml) dans votre fichier `configuration.yaml` de Home Assistant.
* Ajuster Les valeur suivante pour correspondre a votre région à l'aide des tableau plus bas
`{{ state_attr('sensor.msss', 'Numéro de région')[Numéro d'hopital]['Nom_etablissement'] }}`
* Exemple :
`{{ state_attr('sensor.msss', '11')[0]['Nom_etablissement'] }}`

***Les exemples dans les configurations utilise Gaspésie-Îles-de-la-Madeleine (11) et le total régional ([0])***

### Méthode 2
* Ajouter le contenu de fichier [metode2/configuration.yaml](methode2/configuration.yaml) dans votre fichier `configuration.yaml` de Home Assistant.
* Ajuster Les valeur suivante pour correspondre a votre région à l'aide des tableau plus bas
`{{ state_attr('sensor.msss', 'Numéro de région')[Numéro d'hopital]['Nom_etablissement'] }}`
* Exemple :
`{{ state_attr('sensor.msss', '11')[0]['Nom_etablissement'] }}`
* Il est possible de créer différent sensor en utilisant la même formules présente dans [metode2/configuration.yaml](methode2/configuration.yaml) et les différentes type de donnés (Voir tableau plus bas)

## Tableau

<details>
<summary>Liste des établissment du Bas-Saint-Laurent (01)</summary>


# Bas-Saint-Laurent

| Numéro | Installation | Établissement |
|----------|----------|----------|
| 0  | Total régional | Total régional |
| 1  | CENTRE HOSPITALIER RÉGIONAL DU GRAND-PORTAGE | CISSS DU BAS-SAINT-LAURENT |
| 2  | HÔPITAL DE MATANE | CISSS DU BAS-SAINT-LAURENT |
| 3  | CLSC DE POHÉNÉGAMOOK | CISSS DU BAS-SAINT-LAURENT |
| 4  | HÔPITAL NOTRE-DAME-DE-FATIMA | CISSS DU BAS-SAINT-LAURENT |
| 5  | HÔPITAL DE NOTRE-DAME-DU-LAC | CISSS DU BAS-SAINT-LAURENT |
| 6  | HÔPITAL D'AMQUI | CISSS DU BAS-SAINT-LAURENT |
| 7  | HÔPITAL RÉGIONAL DE RIMOUSKI | CISSS DU BAS-SAINT-LAURENT |
| 8  | CENTRE MULTISERVICES DE …CIAUX DE TROIS-PISTOLES | CISSS DU BAS-SAINT-LAURENT |
</details>

<details>
<summary>Liste des établissment du Saguenay-Lac-Saint-Jean (02)</summary>

# Saguenay-Lac-Saint-Jean

| Numéro | Installation | Établissement |
|----------|----------|----------|
| 0  | Total régional | Total régional |
| 1  | HÔPITAL DE CHICOUTIMI | CIUSSS DU SAGUENAY - LAC-SAINT-JEAN |
| 2  | HÔPITAL DE DOLBEAU-MISTASSINI | CIUSSS DU SAGUENAY - LAC-SAINT-JEAN |
| 3  | HÔPITAL D'ALMA | CIUSSS DU SAGUENAY - LAC-SAINT-JEAN |
| 4  | HÔPITAL DE LA BAIE | CIUSSS DU SAGUENAY - LAC-SAINT-JEAN |
| 5  | HÔPITAL ET CENTRE DE RÉADAPTATION DE JONQUIÈRE | CIUSSS DU SAGUENAY - LAC-SAINT-JEAN |
| 6  | HÔPITAL ET CENTRE D'HÉBERGEMENT DE ROBERVAL | CIUSSS DU SAGUENAY - LAC-SAINT-JEAN |

</details>

<details>
<summary>Liste des établissment du Capitale-Nationale (03)</summary>

# Capitale-Nationale

| Numéro | Installation                           | Établissement                            |
|--------|----------------------------------------|-----------------------------------------|
| 0      | Total régional                         | Total régional                           |
| 1      | HÔPITAL DU SAINT-SACREMENT            | CHU DE QUÉBEC - UNIVERSITÉ LAVAL        |
| 2      | L'HÔTEL-DIEU DE QUÉBEC                | CHU DE QUÉBEC - UNIVERSITÉ LAVAL        |
| 3      | CENTRE HOSPITALIER DE L'UNIVERSITÉ LAVAL | CHU DE QUÉBEC - UNIVERSITÉ LAVAL        |
| 4      | HÔPITAL SAINT-FRANÇOIS D'ASSISE       | CHU DE QUÉBEC - UNIVERSITÉ LAVAL        |
| 5      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX CHAUVEAU | CIUSSS DE LA CAPITALE-NATIONALE |
| 6      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE SAINTE-ANNE-DE-BEAUPRÉ | CIUSSS DE LA CAPITALE-NATIONALE  |
| 7      | HÔPITAL ET CLSC DE LA MALBAIE         | CIUSSS DE LA CAPITALE-NATIONALE        |
| 8      | INSTITUT UNIVERSITAIRE DE CARDIOLOGIE ET DE PNEUMOLOGIE DE QUÉBEC | INSTITUT UNIVERSITAIRE DE CARDIOLOGIE ET DE PNEUMOLOGIE DE QUÉBEC - UNIVERSITÉ LAVAL |
| 9      | HÔPITAL DE L'ENFANT-JÉSUS             | CHU DE QUÉBEC - UNIVERSITÉ LAVAL        |
| 10     | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE BAIE-SAINT-PAUL | CIUSSS DE LA CAPITALE-NATIONALE |
| 11     | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE SAINT-RAYMOND | CIUSSS DE LA CAPITALE-NATIONALE |
| 12     | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE SAINT-MARC-DES-CARRIÈRES | CIUSSS DE LA CAPITALE-NATIONALE |

</details>

<details>
<summary>Liste des établissment de la Mauricie et Centre-du-Québec (04)</summary>

# Mauricie et Centre-du-Québec

| Numéro | Installation                                        | Établissement                                     |
|--------|----------------------------------------------------|--------------------------------------------------|
| 0      | Total régional                                      | Total régional                                    |
| 1      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE FORTIERVILLE | CIUSSS DE LA MAURICIE-ET-DU-CENTRE-DU-QUÉBEC |
| 2      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DU HAUT-SAINT-MAURICE | CIUSSS DE LA MAURICIE-ET-DU-CENTRE-DU-QUÉBEC |
| 3      | HÔPITAL DU CENTRE-DE-LA-MAURICIE                   | CIUSSS DE LA MAURICIE-ET-DU-CENTRE-DU-QUÉBEC |
| 4      | PAVILLON SAINTE-MARIE                               | CIUSSS DE LA MAURICIE-ET-DU-CENTRE-DU-QUÉBEC |
| 5      | HÔTEL-DIEU D'ARTHABASKA                            | CIUSSS DE LA MAURICIE-ET-DU-CENTRE-DU-QUÉBEC |
| 6      | HÔPITAL SAINTE-CROIX                                | CIUSSS DE LA MAURICIE-ET-DU-CENTRE-DU-QUÉBEC |
| 7      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX AVELLIN-DALCOURT | CIUSSS DE LA MAURICIE-ET-DU-CENTRE-DU-QUÉBEC |
| 8      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX CHRIST-ROI | CIUSSS DE LA MAURICIE-ET-DU-CENTRE-DU-QUÉBEC |

</details>

<details>
<summary>Liste des établissment de L'Estrie (05)</summary>

# Estrie

| Numéro | Installation                                        | Établissement                                     |
|--------|----------------------------------------------------|--------------------------------------------------|
| 0      | Total régional                                      | Total régional                                    |
| 1      | CHUS - HÔPITAL FLEURIMONT                           | CIUSSS DE L'ESTRIE - CENTRE HOSPITALIER UNIVERSITAIRE DE SHERBROOKE |
| 2      | CHUS - HÔTEL-DIEU DE SHERBROOKE                     | CIUSSS DE L'ESTRIE - CENTRE HOSPITALIER UNIVERSITAIRE DE SHERBROOKE |
| 3      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE MEMPHRÉMAGOG | CIUSSS DE L'ESTRIE - CENTRE HOSPITALIER UNIVERSITAIRE DE SHERBROOKE |
| 4      | CENTRE DE SANTÉ ET DE SERVICES SOCIAUX DU GRANIT     | CIUSSS DE L'ESTRIE - CENTRE HOSPITALIER UNIVERSITAIRE DE SHERBROOKE |
| 5      | HÔPITAL DE GRANBY                                   | CIUSSS DE L'ESTRIE - CENTRE HOSPITALIER UNIVERSITAIRE DE SHERBROOKE |
| 6      | HÔPITAL BROME-MISSISQUOI-PERKINS                   | CIUSSS DE L'ESTRIE - CENTRE HOSPITALIER UNIVERSITAIRE DE SHERBROOKE |
| 7      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DES SOURCES | CIUSSS DE L'ESTRIE - CENTRE HOSPITALIER UNIVERSITAIRE DE SHERBROOKE |
| 8      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE LA MRC DE COATICOOK | CIUSSS DE L'ESTRIE - CENTRE HOSPITALIER UNIVERSITAIRE DE SHERBROOKE |

</details>

<details>
<summary>Liste des établissment de Montréal (06)</summary>

# Montréal

| Numéro | Installation                                     | Établissement                                       |
|--------|--------------------------------------------------|----------------------------------------------------|
| 0      | Total régional                                  | Total régional                                      |
| 1      | HÔPITAL DU SACRÉ-CŒUR DE MONTRÉAL              | CIUSSS DU NORD-DE-L'ÎLE-DE-MONTRÉAL               |
| 2      | HÔPITAL MAISONNEUVE-ROSEMONT                   | CIUSSS DE L'EST-DE-L'ÎLE-DE-MONTRÉAL             |
| 3      | HÔPITAL DE VERDUN                              | CIUSSS DU CENTRE-SUD-DE-L'ÎLE-DE-MONTRÉAL        |
| 4      | CHU SAINTE-JUSTINE                             | CENTRE HOSPITALIER UNIVERSITAIRE SAINTE-JUSTINE |
| 5      | L'HÔPITAL DE MONTRÉAL POUR ENFANTS             | CENTRE UNIVERSITAIRE DE SANTÉ MCGILL            |
| 6      | HÔPITAL ROYAL VICTORIA                        | CENTRE UNIVERSITAIRE DE SANTÉ MCGILL            |
| 7      | HÔPITAL DE LASALLE                            | CIUSSS DE L'OUEST-DE-L'ÎLE-DE-MONTRÉAL          |
| 8      | HÔPITAL GÉNÉRAL DU LAKESHORE                  | CIUSSS DE L'OUEST-DE-L'ÎLE-DE-MONTRÉAL          |
| 9      | HÔPITAL DE LACHINE                            | CENTRE UNIVERSITAIRE DE SANTÉ MCGILL            |
| 10     | HÔPITAL FLEURY                                | CIUSSS DU NORD-DE-L'ÎLE-DE-MONTRÉAL             |
| 11     | HÔPITAL JEAN-TALON                            | CIUSSS DU NORD-DE-L'ÎLE-DE-MONTRÉAL             |
| 12     | HÔPITAL DOUGLAS                               | CIUSSS DE L'EST-DE-L'ÎLE-DE-MONTRÉAL            |
| 13     | HÔPITAL SANTA CABRINI                         | CIUSSS DE L'EST-DE-L'ÎLE-DE-MONTRÉAL            |
| 14     | CENTRE HOSPITALIER DE L'UNIVERSITÉ DE MONTRÉAL | CENTRE HOSPITALIER DE L'UNIVERSITÉ DE MONTRÉAL |
| 15     | HÔPITAL NOTRE-DAME                            | CIUSSS DU CENTRE-SUD-DE-L'ÎLE-DE-MONTRÉAL      |
| 16     | INSTITUT DE CARDIOLOGIE DE MONTRÉAL            | INSTITUT DE CARDIOLOGIE DE MONTRÉAL            |
| 17     | HÔPITAL GÉNÉRAL DE MONTRÉAL                   | CENTRE UNIVERSITAIRE DE SANTÉ MCGILL            |
| 18     | CENTRE HOSPITALIER DE ST. MARY                | CIUSSS DE L'OUEST-DE-L'ÎLE-DE-MONTRÉAL          |
| 19     | HÔPITAL GÉNÉRAL JUIF                          | CIUSSS DU CENTRE-OUEST-DE-L'ÎLE-DE-MONTRÉAL    |
| 20     | HÔPITAL EN SANTÉ MENTALE ALBERT-PRÉVOST       | CIUSSS DU NORD-DE-L'ÎLE-DE-MONTRÉAL             |

</details>

<details>
<summary>Liste des établissment de l'Outaouais (07)</summary>

# Outaouais

| Numéro | Installation                                                       | Établissement                                            |
|--------|--------------------------------------------------------------------|---------------------------------------------------------|
| 0      | Total régional                                                    | Total régional                                            |
| 1      | CISSS DE L'OUTAOUAIS                                               | Total régional                                            |
| 2      | HÔPITAL ET CHSLD DU PONTIAC                                       | CISSS DE L'OUTAOUAIS                                      |
| 3      | CLSC ET CENTRE D'HÉBERGEMENT DE LA PETITE-NATION                   | CISSS DE L'OUTAOUAIS                                      |
| 4      | HÔPITAL DE GATINEAU                                               | CISSS DE L'OUTAOUAIS                                      |
| 5      | HÔPITAL DE HULL                                                   | CISSS DE L'OUTAOUAIS                                      |
| 6      | HÔPITAL DE MANIWAKI                                               | CISSS DE L'OUTAOUAIS                                      |
| 7      | HÔPITAL ET CHSLD MÉMORIAL DE WAKEFIELD / WAKEFIELD MEMORIAL HOSPITAL | CISSS DE L'OUTAOUAIS                                      |
| 8      | HÔPITAL ET CHSLD DE PAPINEAU                                      | CISSS DE L'OUTAOUAIS                                      |
| 9      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE MANSFIELD-ET-PONTEFRACT | CISSS DE L'OUTAOUAIS              |

</details>

<details>
<summary>Liste des établissment de Abitibi-Témiscamingue (08)</summary>

# Abitibi-Témiscamingue

| Numéro | Installation                                                    | Établissement                              |
|--------|-----------------------------------------------------------------|----------------------------------------|
| 0      | Total régional                                                 | Total régional                        |
| 1      | HÔPITAL DE VAL-D'OR                                            | CISSS DE L'ABITIBI-TÉMISCAMINGUE      |
| 2      | HÔPITAL D'AMOS                                                | CISSS DE L'ABITIBI-TÉMISCAMINGUE      |
| 3      | HÔPITAL DE ROUYN-NORANDA                                       | CISSS DE L'ABITIBI-TÉMISCAMINGUE      |
| 4      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE TÉMISCAMING-KIPAWA | CISSS DE L'ABITIBI-TÉMISCAMINGUE  |
| 5      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE VILLE-MARIE | CISSS DE L'ABITIBI-TÉMISCAMINGUE |
| 6      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE LA SARRE | CISSS DE L'ABITIBI-TÉMISCAMINGUE   |

</details>

<details>
<summary>Liste des établissment de la Côte-Nord (09)</summary>

# Côte-Nord

| Numéro | Installation                                                    | Établissement                              |
|--------|-----------------------------------------------------------------|----------------------------------------|
| 0      | Total régional                                                 | Total régional                        |
| 1      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DES ESCOUMINS | CISSS DE LA CÔTE-NORD      |
| 2      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE FORESTVILLE | CISSS DE LA CÔTE-NORD      |
| 3      | CLSC ET HÔPITAL LE ROYER                                       | CISSS DE LA CÔTE-NORD      |
| 4      | HÔPITAL ET CLSC DE SEPT-ÎLES                                   | CISSS DE LA CÔTE-NORD      |
| 5      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE FERMONT | CISSS DE LA CÔTE-NORD   |
| 6      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE LA MINGANIE | CISSS DE LA CÔTE-NORD   |
| 7      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE PORT-CARTIER | CISSS DE LA CÔTE-NORD |
| 8      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE LA BASSE-CÔTE-NORD | CISSS DE LA CÔTE-NORD |

</details>

<details>
<summary>Liste des établissment de la Gaspésie-Îles-de-la-Madeleine (11)</summary>

# Gaspésie-Îles-de-la-Madeleine

| Numéro | Installation                                            | Établissement                                         |
|--------|---------------------------------------------------------|-------------------------------------------------------|
| 0      | Total régional                                         | Total régional                                    |
| 1      | HÔPITAL DE GASPÉ                                      | CISSS DE LA GASPÉSIE                         |
| 2      | CLSC ET CENTRE DE SERVICES AMBULATOIRES DE PASPÉBIAC   | CISSS DE LA GASPÉSIE                         |
| 3      | CLSC ET CENTRE DE SERVICES AMBULATOIRES DE MURDOCHVILLE | CISSS DE LA GASPÉSIE                         |
| 4      | HÔPITAL DE CHANDLER                                   | CISSS DE LA GASPÉSIE                         |
| 5      | HÔPITAL DE L'ARCHIPEL                                | CISSS DES ÎLES                                   |
| 6      | HÔPITAL ET GROUPE DE MÉDECINE DE FAMILLE UNIVERSITAIRE DE MARIA | CISSS DE LA GASPÉSIE                         |
| 7      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE GRANDE-VALLÉE | CISSS DE LA GASPÉSIE                         |
| 8      | HÔPITAL ET CLSC DE SAINTE-ANNE-DES-MONTS               | CISSS DE LA GASPÉSIE                         |

</details>

<details>
<summary>Liste des établissment de Chaudière-Appalaches (12)</summary>

# Chaudière-Appalaches

| Numéro | Installation                                            | Établissement                                         |
|--------|---------------------------------------------------------|-------------------------------------------------------|
| 0      | Total régional                                         | Total régional                                    |
| 1      | HÔTEL-DIEU DE LÉVIS                                   | CISSS DE CHAUDIÈRE-APPALACHES                    |
| 2      | HÔPITAL DE SAINT-GEORGES                              | CISSS DE CHAUDIÈRE-APPALACHES                    |
| 3      | CHSLD ET HÔPITAL PAUL-GILBERT                        | CISSS DE CHAUDIÈRE-APPALACHES                    |
| 4      | HÔPITAL DE MONTMAGNY                                 | CISSS DE CHAUDIÈRE-APPALACHES                    |
| 5      | HÔPITAL DE THETFORD                                  | CISSS DE CHAUDIÈRE-APPALACHES                    |

</details>

<details>
<summary>Liste des établissment de Laval (13)</summary>

# Laval

| Numéro | Installation                                  | Établissement                  |
|--------|-----------------------------------------------|--------------------------------|
| 0      | Total régional                               | Total régional                 |
| 1      | HÔPITAL DE LA CITÉ-DE-LA-SANTÉ               | CISSS DE LAVAL                |

</details>

<details>
<summary>Liste des établissment de Lanaudière (14)</summary>

# Lanaudière

| Numéro | Installation                                            | Établissement                                         |
|--------|---------------------------------------------------------|-------------------------------------------------------|
| 0      | Total régional                                         | Total régional                                    |
| 1      | HÔPITAL PIERRE-LE GARDEUR                             | CISSS DE LANAUDIÈRE                              |
| 2      | HÔPITAL DE LANAUDIÈRE ET CENTRE D'HÉBERGEMENT PARPHILIA-FERLAND | CISSS DE LANAUDIÈRE |

</details>

<details>
<summary>Liste des établissment des Laurentides (15)</summary>

# Laurentides

| Numéro | Installation                                            | Établissement                                         |
|--------|---------------------------------------------------------|-------------------------------------------------------|
| 0      | Total régional                                         | Total régional                                    |
| 1      | HÔPITAL DE MONT-LAURIER                              | CISSS DES LAURENTIDES                            |
| 2      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE RIVIÈRE-ROUGE | CISSS DES LAURENTIDES |
| 3      | HÔPITAL DE SAINT-EUSTACHE                            | CISSS DES LAURENTIDES                            |
| 4      | HÔPITAL DE SAINT-JÉRÔME                             | CISSS DES LAURENTIDES                            |
| 5      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX D'ARGENTEUIL | CISSS DES LAURENTIDES |
| 6      | CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE SAINTE-AGATHE | CISSS DES LAURENTIDES |

</details>

<details>
<summary>Liste des établissment de la Montérégie (16)</summary>

# Montérégie

| Numéro | Installation                                            | Établissement                                         |
|--------|---------------------------------------------------------|-------------------------------------------------------|
| 0      | Total régional                                         | Total régional                                    |
| 1      | HÔPITAL BARRIE MEMORIAL / BARRIE MEMORIAL HOSPITAL   | CISSS DE LA MONTÉRÉGIE-OUEST                    |
| 2      | HÔPITAL PIERRE-BOUCHER                                | CISSS DE LA MONTÉRÉGIE-EST                      |
| 3      | HÔPITAL DU HAUT-RICHELIEU                            | CISSS DE LA MONTÉRÉGIE-CENTRE                   |
| 4      | HÔTEL-DIEU DE SOREL                                  | CISSS DE LA MONTÉRÉGIE-EST                      |
| 5      | HÔPITAL DU SUROÎT                                   | CISSS DE LA MONTÉRÉGIE-OUEST                    |
| 6      | HÔPITAL ANNA-LABERGE                                | CISSS DE LA MONTÉRÉGIE-OUEST                    |
| 7      | HÔPITAL HONORÉ-MERCIER                              | CISSS DE LA MONTÉRÉGIE-EST                      |
| 8      | HÔPITAL CHARLES-LE MOYNE                            | CISSS DE LA MONTÉRÉGIE-CENTRE                   |

</details>

<details>
<summary>Liste des établissment de l'Ensemble du Québec (99)</summary>

# Ensemble du Québec

| Numéro | Installation                 | Établissement             |
|--------|------------------------------|---------------------------|
| 0      | Ensemble du Québec          | Ensemble du Québec       |

</details>

## TODO

- Améliorer le JSON résultant
- Ajouté un dashboard Lovalace
