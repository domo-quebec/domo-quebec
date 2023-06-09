# CAA

**En développement, bienvenu aux contributions**

## Extractions des données
Le CAA publie le prix de l'essence par région sur son site [https://www.caa.ca/fr/prix-de-lessence/](https://www.caa.ca/fr/prix-de-lessence/)

Il est possible d'extraire ces données en format json avec la commande suivante: `curl -s --request POST "https://www.caa.ca/wp/wp-admin/admin-ajax.php" --form action=getCitiesForDropdown --form caa_dropdown=QUEBEC`

## Installation

### Capteurs

Les valeurs du fichier [configuration.yaml](configuration.yaml) doivent être ajoutées à votre configuration. Prenez soin d'ajuster les valeurs afin de refléter la région pour laquelle vous voulez les données. Attention, les majuscules doivent être respectées.

L'icon varie selon la variation du prix pour désactiver le changement d'icon, seulement remplacée :

   ```
   icon: >
          {% if state_attr('sensor.caa_prix_essence_data', 'arrow')['MONTREAL'] == "up"  %}
            mdi:arrow-up
          {% elif state_attr('sensor.caa_prix_essence_data', 'arrow')['MONTREAL'] == "equal"  %}
            mdi:equal
          {% elif state_attr('sensor.caa_prix_essence_data', 'arrow')['MONTREAL'] == "down"  %}
            mdi:arrow-down
          {% endif %}
   ```
        
        
par : ```icon: mdi:gas-station```

Les exemples utilisent la région de Montréal, les autres régions possibles jusqu'à maintenant sont inscrites dans le tableau ci-bas.

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

## TODO

- Dashboard lovelace
