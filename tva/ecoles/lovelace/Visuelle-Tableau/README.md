# HqCombo Page

### Installation

- Install [Hydroqc Add-on](https://hydroqc.ca/fr/docs/installation/hass-addon/) 
- Install [Swiss Army Knife Custom Card](https://github.com/amoebelabs/swiss-army-knife-card/).
- Install vertical-stack-in-card from [HACS]
- Install Apexcharts-card from [HACS] 
- Copy the folowing templates in /config/lovelace/sak_templates/templates/layouts/ directory
  - sak-layout-mjt-kwh-total-previsions.yaml
  - sak-layout-mjt-moyennes.yaml
  - sak-layout-mjt-jours-prevision-kwh-periode.yaml
  - sak-layout-mjt-production-demande.yaml
- Copy theme in /config/themes/ directory
- Copy the HqCombo.yaml

- Add the following sensors in the file sensor.yaml

```
# États des période Hydro-Québec
sensor:
  - platform: template
    sensors:
      etat_hydroqc_maison_next_or_current_outage:
        unique_id: "etat_hydroqc_maison_next_or_current_outage"
        friendly_name: "Période de pannes prévues"
        icon_template: mdi:transmission-tower
        value_template: >
          {% if is_state('sensor.hydroqc_maison_next_or_current_outage', 'unavailable') %}
            Aucune 
          {% else %}
            {% set heure = as_timestamp(states('sensor.hydroqc_maison_next_or_current_outage')) | timestamp_custom('%H:%M') %}
            {% set journee = ["Lun", "Mar","Mer","Jeu","Ven","Sam","Dim"] %}
            {{ journee[as_timestamp(states('sensor.hydroqc_maison_next_or_current_outage')) | timestamp_custom('%w' ) | int -1 ] }} {{ heure }}
          {% endif %}
        
  - platform: template
    sensors:
      etat_hydroqc_maison_next_pre_heat_start:
        unique_id: "etat_hydroqc_maison_next_pre_heat_start"
        friendly_name: "Prochaine période de pré-chauffage"
        icon_template: mdi:radiator
        value_template: >
          {% if is_state('sensor.hydroqc_maison_next_pre_heat_start', 'unavailable') %}
            Inactif
          {% else %}
            {% set heure = as_timestamp(states('sensor.hydroqc_maison_next_pre_heat_start')) | timestamp_custom('%H:%M') %}
            {% set journee = ["Lun", "Mar","Mer","Jeu","Ven","Sam","Dim"] %}
            {{ journee[as_timestamp(states('sensor.hydroqc_maison_next_pre_heat_start')) | timestamp_custom('%w' ) | int -1 ] }} {{ heure }}
          {% endif %}
        
  - platform: template
    sensors:
      etat_hydroqc_maison_next_peak_start:
        unique_id: "etat_hydroqc_maison_next_peak_start"
        friendly_name: "Début de la prochaine période de pointe"
        icon_template: mdi:clock-start
        value_template: >
          {% if is_state('sensor.hydroqc_maison_next_peak_start', 'unavailable') %}
            Inactif
          {% else %}
            {% set heure = as_timestamp(states('sensor.hydroqc_maison_next_peak_start')) | timestamp_custom('%H:%M') %}
            {% set journee = ["Lun", "Mar","Mer","Jeu","Ven","Sam","Dim"] %}
            {{ journee[as_timestamp(states('sensor.hydroqc_maison_next_peak_start')) | timestamp_custom('%w' ) | int -1 ] }} {{ heure }}
          {% endif %}
        
  - platform: template
    sensors:
      etat_hydroqc_maison_next_peak_end:
        unique_id: "etat_hydroqc_maison_next_peak_end"
        friendly_name: "Fin de la prochaine période de pointe"
        icon_template: mdi:clock-end
        value_template: >
          {% if is_state('sensor.hydroqc_maison_next_peak_end', 'unavailable') %}
            Inactif
          {% else %}
            {% set heure = as_timestamp(states('sensor.hydroqc_maison_next_peak_end')) | timestamp_custom('%H:%M') %}
          {% set journee = ["Lun", "Mar","Mer","Jeu","Ven","Sam","Dim"] %}
            {{ journee[as_timestamp(states('sensor.hydroqc_maison_next_peak_end')) | timestamp_custom('%w' ) | int -1 ] }} {{ heure }}
          {% endif %}
        
```

- Restart Home Assistant

## Screenshots

![image](https://user-images.githubusercontent.com/83040228/220205161-9e73412a-c230-4c8f-9c11-0602cbc84e00.jpeg)

![image](https://user-images.githubusercontent.com/83040228/220217800-63401835-1d67-4681-861e-f144fed58e2a.jpeg)


### Changelog
#### 1.0
- First release

