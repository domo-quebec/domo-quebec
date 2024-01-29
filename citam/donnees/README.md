# Données

## Liste des ID de villes

Pour obtenir la liste des villes vous devez vous connecter au portail CITAM avec votre compte.

Une fois connecté ouvrez un outil de developpement de votre furteur et allez dans la section "Inscrivez-vous",
vous verrez une requête à `https://massalert.citam.ca/api/Cities/AllCitiesForSelection` qui retourne l'ensemble des villes.

## Alertes en cours

La liste d'alerte en cours pour une ville est publique et peux être accédée via l'URL suivant:

https://massalert.citam.ca/api/Alerts/Triggered/((votre id de ville))

Il est important de noté que selon l'utilisation que la ville en fait, les alertes ne sont pas nécessairement toujours publiées sur le site,
il est possible de faire une alerte téléphonique uniquement par exemple qui ne sera pas affiché sur le site.
