# CAA

Le CAA publie le prix de l'essence par région sur son site [https://www.caa.ca/fr/prix-de-lessence/](https://www.caa.ca/fr/prix-de-lessence/)

Il est possible d'extraire ces données en format json avec la commande suivante: `curl -s --request POST "https://www.caa.ca/wp/wp-admin/admin-ajax.php" --form action=getCitiesForDropdown --form caa_dropdown=QUEBEC`