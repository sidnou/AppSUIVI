# Application
"""
Descrition:

La application serre à enregistrer des numéros de suivi, afin de préparer une feuille de colisage pour Chronopost

Il peut être utilisé par un lecteur de code barre ou Qrcode de préférence.
Démarrage de l'application
    Créer fichier temporaire en format json
    Ou
    Charge les données saisies non enregistrées, si disponible.
    Enregistrement automatique tous les 5s
    Supprime le fichier temporaire json une fois Imprimé

Première étape:
    Valeur saisie par lecteur ou manuel.
        Vérification de la longueur valeur
            Si la valeur saisie est de longueur de 13, commence XR et finis par FR (exemple: XR123456789FR)
            si la valeur saisie est de longueur supérieure à 13, une recherche approfondie

        Vérification des numéros de suivi doublons saisie
            Retourne Erreur de doublon

Seconde étape:
    Enregistrement dans la basse de donnée.
        - SQLite (local).
        - Postgresql (en ligne Serveur). Consultable avec application web


Troisième étape:
    Impression de la feuille formatée colisage pour Chronopost


"""

