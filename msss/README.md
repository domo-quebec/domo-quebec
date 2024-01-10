# MSSS

**En développement, bienvenu aux contributions**

Le ministère de la Santé et des Services sociaux publie plusieurs données.

## État d'occupation des urgences (horaire)

Un fichier CSV est rafraichi à chaque heure environ et est disponible à l'adresse suivante : [https://www.msss.gouv.qc.ca/professionnels/statistiques/documents/urgences/Releve_horaire_urgences_7jours_nbpers.csv](https://www.msss.gouv.qc.ca/professionnels/statistiques/documents/urgences/Releve_horaire_urgences_7jours_nbpers.csv)

Le format CSV se prête mal à l'interprétation des données et ce fichier plus particulièrement comporte plusieurs irrégularités au niveau de caractère superflu. Un petit script python permet de nettoyer les données et les convertir au format json.

## Installation

Première étape, copier le fichier "getmsssdata.py" sous le répertoire "/config/python_scripts/".

Deuxième étape, ajouter le code du fichier [configuration.yaml](configuration.yaml) dans votre configuration. Prenez soin d'ajuster les valeurs sous " json_attributes" afin de refléter les régions pour lesquelles vous voulez extraire les données. Les régions possibles jusqu'à maintenant sont inscrites dans les tableaux plus bas. Dans le code ci-dessous, les régions 6, 13, 14, 15 et 99 sont indiqués.

```
command_line:
  - sensor:
      name: MSSS Etat occupation des urgences
      unique_id: MSSS_urgences_data
      value_template: '{{ value_json.99.Mise_a_jour | as_datetime | as_local }}'
      device_class: timestamp
      command: 'python3 /config/python_scripts/getmsssdata.py'
      json_attributes:
      - "06"
      - "13"
      - "14"
      - "15"
      - "99"
      scan_interval: 3600
```
## Capteurs

Les valeurs du fichier [configuration.yaml](configuration.yaml) doivent être ajoutées à votre configuration. Prenez soin d'ajuster les valeurs afin de refléter la région et le nom de l'installation pour laquelle vous voulez les données. Attention, les majuscules doivent être respectées.

Les attributs peuvent être utilisés pour la définition des capteurs :

  * Nom_etablissement
  * Nom_installation
  * No_permis_installation
  * Nombre_de_civieres_fonctionnelles
  * Nombre_de_civieres_occupees
  * Nombre_de_patients_sur_civiere_plus_de_24_heures
  * Nombre_de_patients_sur_civiere_plus_de_48_heures
  * Nombre_total_de_patients_presents_a_lurgence
  * Nombre_total_de_patients_en_attente_de_PEC
  * DMS_sur_civiere
  * DMS_ambulatoire
  * DMS_sur_civiere_horaire
  * DMS_ambulatoire_horaire
  * Heure_de_lextraction_image
  * Mise_a_jour

* L'acronyme PEC signifi : Prise en Charge
* L'acronyme DMS signifi : Durée moyenne du séjour.

### Note : Le code ci-dessous donne un appercu, utilisez le code directement dans le fichier [configuration.yaml](configuration.yaml) pour un plus large éventail d'exemple.

```
template:
  - sensor:
    - name: msss_99_region
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].Region }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
  - sensor:
    - name: msss_99_nom
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].Nom_installation }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
  - sensor:
    - name: msss_99_patient
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].Nombre_total_de_patients_presents_a_lurgence }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
  - sensor:
    - name: msss_99_patient_pec
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].Nombre_total_de_patients_en_attente_de_PEC }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
  - sensor:
    - name: msss_99_patient_dms
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].DMS_ambulatoire_horaire }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
  - sensor:
    - name: msss_99_mise_a_jour
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].Mise_a_jour }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
  - sensor:
    - name: msss_99_extraction
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].Heure_de_lextraction_image }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
  - sensor:
    - name: msss_99_civieres_occupees
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].Nombre_de_civieres_occupees }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
  - sensor:
    - name: msss_99_civieres_24h
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].Nombre_de_patients_sur_civiere_plus_de_24_heures }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
  - sensor:
    - name: msss_99_civieres_48h
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].Nombre_de_patients_sur_civiere_plus_de_48_heures }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
  - sensor:
    - name: msss_99_civieres_dms
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].DMS_sur_civiere | round(2) }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
```

Les exemples suivants utilisent différentes régions afin de vous familiariser, les régions possibles jusqu'à maintenant sont inscrites dans les tableaux ci-bas.

Exemple pour un senseur du nom de l'établissement "HÔPITAL DE MATANE" de la région du Bas Saint-Laurent. Région 1 Index 2.

```
  - sensor:
    - name: msss_01_matane_nom
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '01') [2].Nom_installation }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '01') is not none }}"
```
      
Autre exemple pour un senseur du nombre de patients présent à l'urgence de l'établissement "HÔPITAL D'ALMA" de la région du Saguenay-Lac-Saint-Jean. Région 2 Index 3.

```
  - sensor:
    - name: msss_02_juif_patient
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '02') [3].Nombre_total_de_patients_presents_a_lurgence }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '02') is not none }}"
```

Dernier exemple pour un senseur du nombre de patients sur civiere pour plus de 48 heures à l'urgence de la région Ensemble du Québec. Région 99 Index 0.

```
  - sensor:
    - name: msss_99_civieres_48h
      state: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') [0].Nombre_de_patients_sur_civiere_plus_de_48_heures }}"
      availability: "{{ state_attr('sensor.msss_etat_occupation_des_urgences', '99') is not none }}"
```      

| Région 1 - Bas-Saint-Laurent |
|-------|
| Index 0 - Total régional |
| Index 1 - CENTRE HOSPITALIER RÉGIONAL DU GRAND-PORTAGE |
| Index 2 - HÔPITAL DE MATANE |
| Index 3 - CLSC DE POHÉNÉGAMOOK |
| Index 4 - HÔPITAL NOTRE-DAME-DE-FATIMA |
| Index 5 - HÔPITAL DE NOTRE-DAME-DU-LAC |
| Index 6 - HÔPITAL D'AMQUI |
| Index 7 - HÔPITAL RÉGIONAL DE RIMOUSKI |
| Index 8 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE TROIS-PISTOLES |

| Région 2 - Saguenay-Lac-Saint-Jean |
|-------|
| Index 0 - Total régional |
| Index 1 - HÔPITAL DE CHICOUTIMI |
| Index 2 - HÔPITAL DE DOLBEAU-MISTASSINI |
| Index 3 - HÔPITAL D'ALMA |
| Index 4 - HÔPITAL DE LA BAIE |
| Index 5 - HÔPITAL ET CENTRE DE RÉADAPTATION DE JONQUIÈRE |
| Index 6 - HÔPITAL ET CENTRE D'HÉBERGEMENT DE ROBERVAL |

| Région 3 - Capitale-Nationale |
|-------|
| Index 0 - Total régional |
| Index 1 - HÔPITAL DU SAINT-SACREMENT |
| Index 2 - L'HÔTEL-DIEU DE QUÉBEC |
| Index 3 - CENTRE HOSPITALIER DE L'UNIVERSITÉ LAVAL |
| Index 4 - HÔPITAL SAINT-FRANÇOIS D'ASSISE |
| Index 5 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX CHAUVEAU |
| Index 6 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE SAINTE-ANNE-DE-BEAUPRÉ |
| Index 7 - HÔPITAL ET CLSC DE LA MALBAIE |
| Index 8 - INSTITUT UNIVERSITAIRE DE CARDIOLOGIE ET DE PNEUMOLOGIE DE QUÉBEC |
| Index 9 - HÔPITAL DE L'ENFANT-JÉSUS |
| Index 10 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE BAIE-SAINT-PAUL |
| Index 11 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE SAINT-RAYMOND |
| Index 12 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE SAINT-MARC-DES-CARRIÈRES |

| Région 4 - Mauricie et Centre-du-Québec |
|-------|
| Index 0 - Total régional |
| Index 1 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE FORTIERVILLE |
| Index 2 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DU HAUT-SAINT-MAURICE |
| Index 3 - HÔPITAL DU CENTRE-DE-LA-MAURICIE |
| Index 4 - PAVILLON SAINTE-MARIE |
| Index 5 - HÔTEL-DIEU D'ARTHABASKA |
| Index 6 - HÔPITAL SAINTE-CROIX |
| Index 7 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX AVELLIN-DALCOURT |
| Index 8 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX CHRIST-ROI |

| Région 5 - Estrie |
|-------|
| Index 0 - Total régional |
| Index 1 - CHUS - HÔPITAL FLEURIMONT |
| Index 2 - CHUS - HÔTEL-DIEU DE SHERBROOKE |
| Index 3 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE MEMPHRÉMAGOG |
| Index 4 - CENTRE DE SANTÉ ET DE SERVICES SOCIAUX DU GRANIT |
| Index 5 - HÔPITAL DE GRANBY |
| Index 6 - HÔPITAL BROME-MISSISQUOI-PERKINS |
| Index 7 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DES SOURCES |
| Index 8 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE LA MRC DE COATICOOK |

| Région 6 - Montréal |
|-------|
| Index 0 - Total régional |
| Index 1 - HÔPITAL DU SACRÉ-CŒUR DE MONTRÉAL |
| Index 2 - HÔPITAL MAISONNEUVE-ROSEMONT |
| Index 3 - HÔPITAL DE VERDUN |
| Index 4 - CHU SAINTE-JUSTINE |
| Index 5 - L'HÔPITAL DE MONTRÉAL POUR ENFANTS |
| Index 6 - HÔPITAL ROYAL VICTORIA |
| Index 7 - HÔPITAL DE LASALLE |
| Index 8 - HÔPITAL GÉNÉRAL DU LAKESHORE |
| Index 9 - HÔPITAL DE LACHINE |
| Index 10 - HÔPITAL FLEURY |
| Index 11 - HÔPITAL JEAN-TALON |
| Index 12 - HÔPITAL DOUGLAS |
| Index 13 - HÔPITAL DE SOINS PSYCHIATRIQUES DE L'EST-DE-MONTRÉAL |
| Index 14 - HÔPITAL SANTA CABRINI |
| Index 15 - CENTRE HOSPITALIER DE L'UNIVERSITÉ DE MONTRÉAL |
| Index 16 - HÔPITAL NOTRE-DAME |
| Index 17 - INSTITUT DE CARDIOLOGIE DE MONTRÉAL |
| Index 18 - HÔPITAL GÉNÉRAL DE MONTRÉAL |
| Index 19 - CENTRE HOSPITALIER DE ST. MARY |
| Index 20 - HÔPITAL GÉNÉRAL JUIF |
| Index 11 - HÔPITAL EN SANTÉ MENTALE ALBERT-PRÉVOST |

| Région 7 - Outaouais |
|-------|
| Index 0 - Total régional |
| Index 1 - HÔPITAL ET CHSLD DU PONTIAC |
| Index 2 - CLSC ET CENTRE D'HÉBERGEMENT DE LA PETITE-NATION |
| Index 3 - HÔPITAL DE GATINEAU |
| Index 4 - HÔPITAL DE HULL |
| Index 5 - HÔPITAL DE MANIWAKI |
| Index 6 - HÔPITAL ET CHSLD MÉMORIAL DE WAKEFIELD / WAKEFIELD MEMORIAL HOSPITAL |
| Index 7 - HÔPITAL ET CHSLD DE PAPINEAU |
| Index 8 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE MANSFIELD-ET-PONTEFRACT |

| Région 8 - Témiscamingue |
|-------|
| Index 0 - Total régional |
| Index 1 - HÔPITAL DE VAL-D'OR |
| Index 2 - HÔPITAL D'AMOS |
| Index 3 - HÔPITAL DE ROUYN-NORANDA |
| Index 4 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE TÉMISCAMING-KIPAWA |
| Index 5 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE VILLE-MARIE |
| Index 6 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE LA SARRE |

| Région 9 - Côte-Nord |
|-------|
| Index 0 - Total régional |
| Index 1 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DES ESCOUMINS |
| Index 2 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE FORESTVILLE |
| Index 3 - CLSC ET HÔPITAL LE ROYER |
| Index 4 - HÔPITAL ET CLSC DE SEPT-ÎLES |
| Index 5 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE FERMONT |
| Index 6 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE LA MINGANIE |
| Index 7 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE PORT-CARTIER |
| Index 8 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE LA BASSE-CÔTE-NORD |

| Région 11 - Gaspésie-Îles-de-la-Madeleine |
|-------|
| Index 0 - Total régional |
| Index 1 - HÔPITAL DE GASPÉ |
| Index 2 - CLSC ET CENTRE DE SERVICES AMBULATOIRES DE PASPÉBIAC |
| Index 3 - CLSC ET CENTRE DE SERVICES AMBULATOIRES DE MURDOCHVILLE |
| Index 4 - HÔPITAL DE CHANDLER |
| Index 5 - HÔPITAL DE L'ARCHIPEL |
| Index 6 - HÔPITAL ET GROUPE DE MÉDECINE DE FAMILLE UNIVERSITAIRE DE MARIA |
| Index 7 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE GRANDE-VALLÉE |
| Index 8 - HÔPITAL ET CLSC DE SAINTE-ANNE-DES-MONTS |

| Région 12 - Chaudière-Appalaches |
|-------|
| Index 0 - Total régional |
| Index 1 - HÔTEL-DIEU DE LÉVIS |
| Index 2 - HÔPITAL DE SAINT-GEORGES |
| Index 3 - CHSLD ET HÔPITAL PAUL-GILBERT |
| Index 4 - HÔPITAL DE MONTMAGNY |
| Index 5 - HÔPITAL DE THETFORD |

| Région 13 - Laval |
|-------|
| Index 0 - Total régional |
| Index 1 - HÔPITAL DE LA CITÉ-DE-LA-SANTÉ |

| Région 14 - Lanaudière |
|-------|
| Index 0 - Total régional |
| Index 1 - HÔPITAL PIERRE-LE GARDEUR |
| Index 2 - HÔPITAL DE LANAUDIÈRE ET CENTRE D'HÉBERGEMENT PARPHILIA-FERLAND |

| Région 15 - Laurentides |
|-------|
| Index 0 - Total régional |
| Index 1 - HÔPITAL DE MONT-LAURIER |
| Index 2 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE RIVIÈRE-ROUGE |
| Index 3 - HÔPITAL DE SAINT-EUSTACHE |
| Index 4 - HÔPITAL DE SAINT-JÉRÔME |
| Index 5 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX D'ARGENTEUIL |
| Index 6 - CENTRE MULTISERVICES DE SANTÉ ET DE SERVICES SOCIAUX DE SAINTE-AGATHE |

| Région 16 - Montérégie |
|-------|
| Index 0 - Total régional |
| Index 1 - HÔPITAL BARRIE MEMORIAL / BARRIE MEMORIAL HOSPITAL |
| Index 2 - HÔPITAL PIERRE-BOUCHER |
| Index 3 - HÔPITAL DU HAUT-RICHELIEU |
| Index 4 - HÔTEL-DIEU DE SOREL |
| Index 5 - HÔPITAL DU SUROÎT |
| Index 6 - HÔPITAL ANNA-LABERGE |
| Index 7 - HÔPITAL HONORÉ-MERCIER |
| Index 8 - HÔPITAL CHARLES-LE MOYNE |

| Région 99 - Ensemble du Québec |
|-------|
| Index 0 - Ensemble du Québec |


## TODO

