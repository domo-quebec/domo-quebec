#  Prix de l'essence

Ce répertoire inclu plusieurs cartes pour affiher le prix de l'essenece actuel et celui d'hier.

## Carte Apexcharts

### Installation

- Installer [Apexcharts](https://github.com/RomRider/apexcharts-card) depuis le HACS.
- Copier le fichier caa_apexcharts_card.yaml dans votre environnement.

<img width="622" alt="image" src="https://github.com/MichelJourdain/domo-quebec/assets/83040228/20bb1755-bdf9-4370-abb9-b44b651763df">

## Carte Mini Graph

### Installation

- Installer [Mini-graph](https://github.com/RomRider/apexcharts-card) depuis le HACS.
- Copier le fichier caa_mini_graph_card_button_card.yaml dans votre environnement.

<img width="626" alt="image" src="https://github.com/MichelJourdain/domo-quebec/assets/83040228/21947e5d-2eb7-44fb-8cac-5df2de97b47f">

## Carte Multiple entity row

### Installation

- Installer [multiple-entity-row](https://github.com/RomRider/apexcharts-card) depuis le HACS.
- Copier le fichier caa_multiple_entity_row_card.yaml dans votre environnement.
- Ajouter les sensors pour les ville que vous voulez suivrent dans le fichier de configuration.
  - Exemple:
 
 ```
   - sensor:
    - name: "CAA Prix Essence Trois-rivières Aujourd'hui"
      unique_id: caa_gas_today_trois_rivieres
      icon: >
        {% if state_attr('sensor.caa_prix_essence_data', 'arrow')['TROIS-RIVIERES'] == "up"  %}
          mdi:arrow-up-bold-circle
        {% elif state_attr('sensor.caa_prix_essence_data', 'arrow')['TROIS-RIVIERES'] == "equal"  %}
          mdi:equal
        {% elif state_attr('sensor.caa_prix_essence_data', 'arrow')['TROIS-RIVIERES'] == "down"  %}
          mdi:arrow-down-bold-circle
        {% endif %}
      device_class: monetary
      unit_of_measurement: "CAD/L"
      state: >
        {% set val2 = state_attr('sensor.caa_prix_essence_data', 'today')['TROIS-RIVIERES'] | float / 100 %}
        {{ val2 | round(3) }}
      attributes:
        attribution: Données fournies par CAA Québec
        arrow: >
          {{ state_attr('sensor.caa_prix_essence_data', 'arrow')['TROIS-RIVIERES'] }}
        yesterday: >
          {{ state_attr('sensor.caa_prix_essence_data', 'yesterday')['TROIS-RIVIERES'] }}
          
  - sensor:
    - name: "CAA Prix Essence Trois-Rivières hier"
      unique_id: caa_gas_yesterday_trois_rivieres
      icon: mdi:arrow-left-top-bold
      device_class: monetary
      unit_of_measurement: "CAD/L"
      state: >
       {% set val3 = state_attr('sensor.caa_prix_essence_data', 'yesterday')['TROIS-RIVIERES'] | float / 100 %}
       {{ val3 | round(3) }}
       
  - sensor:
    - name: "CAA Prix Essence Montréal Aujourd'hui"
      unique_id: caa_gas_today_montreal
      icon: >
        {% if state_attr('sensor.caa_prix_essence_data', 'arrow')['MONTREAL'] == "up"  %}
          mdi:arrow-up-bold-circle
        {% elif state_attr('sensor.caa_prix_essence_data', 'arrow')['MONTREAL'] == "equal"  %}
          mdi:equal
        {% elif state_attr('sensor.caa_prix_essence_data', 'arrow')['MONTREAL'] == "down"  %}
          mdi:arrow-down-bold-circle
        {% endif %}
      device_class: monetary
      unit_of_measurement: "CAD/L"
      state: >
        {% set val4 = state_attr('sensor.caa_prix_essence_data', 'today')['MONTREAL'] | float / 100 %}
        {{ val4 | round(3) }}
      attributes:
        attribution: Données fournies par CAA Québec
        arrow: >
          {{ state_attr('sensor.caa_prix_essence_data', 'arrow')['MONTREAL'] }}
        yesterday: >
          {{ state_attr('sensor.caa_prix_essence_data', 'yesterday')['MONTREAL'] }}

  - sensor:
    - name: "CAA Prix Essence Montréal hier"
      unique_id: caa_gas_yesterday_montreal
      icon: mdi:arrow-left-top-bold
      device_class: monetary
      unit_of_measurement: "CAD/L"
      state: >
       {% set val5 = state_attr('sensor.caa_prix_essence_data', 'yesterday')['MONTREAL'] | float / 100 %}
       {{ val5 | round(3) }}
```
<img width="625" alt="image" src="https://github.com/MichelJourdain/domo-quebec/assets/83040228/dca99502-039c-494e-ad68-48c0e675c5a5">


## Carte mushroom chips card

### Installation

- Installer [Mushroom](https://github.com/RomRider/apexcharts-card) depuis le HACS.
- Copier le fichier caa_mushroom_chips_card_prix_aujourdhui.yaml dans votre environnement pour avoir le prix actuel.
- Copier le fichier caa_mushroom_chips_card_prix_aujourdhui_hier.yaml dans votre environnement pour avoir le prix actuel et celui d'hier.

<img width="114" alt="image" src="https://github.com/MichelJourdain/domo-quebec/assets/83040228/b18b1bc7-9ae8-4867-9e7c-0740905ae84a">
<img width="218" alt="image" src="https://github.com/MichelJourdain/domo-quebec/assets/83040228/ccb87420-f051-425a-9d3d-9bb6b5bbcc2d">

