# MSSS

Le ministère de la Santé et des Services sociaux publie plusieurs données.

## État d'occupation des urgences (horaire)

Un fichier CSV est rafraichi à chaque heure environ et est disponible à l'adresse suivante : [https://www.msss.gouv.qc.ca/professionnels/statistiques/documents/urgences/Releve_horaire_urgences_7jours_nbpers.csv](https://www.msss.gouv.qc.ca/professionnels/statistiques/documents/urgences/Releve_horaire_urgences_7jours_nbpers.csv)

Le format CSV se prête mal à l'interprétation des données et ce fichier plus particulièrement comporte plusieurs irrégularités au niveau de caractère superflu. Un petit script python permet de nettoyer les données et les convertir au format json.