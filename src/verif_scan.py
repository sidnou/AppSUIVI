import re

'''
Script de verification qrcode scanné 

- Recuperation des données spécifique 
    ex: Numéro dossier M67S-AAMM-NNNNN (15 caratère incluant "-")
        Numéro Suivi XRXXXXXXXXXFR (13 Caractères)


A partir de n'importe que données scanné QRcode ou code barre
- la longeur des code bare du numéro suivi sont 13
- la longeur des qrcode sont superieurs a 13 


Exemple longeur de 
XS410656256FR   ( 13 caractères )
Ex%0057470XS410656256248848901 (30 caractères) 

[)>01020057470901848XS410656256248GEOP5357250321/1.5KGN115 Rue des RomainsHOMBOURG HAUTEpicerie La Chapelle07G03000HILLEBRAND Joris0663667039joris.hillebrand4@gmail.com1.5KGM67S-2601-00292M67S-2601-00292N007S010Maintronic/OCI03902279402 Rue Andre Marie AmpereMundolsheim6745025007D001011210126XS410656256FR00000M67S-2601-   ]
(environ 3832 Caractères)

'''


def scan_verif(data_scan):
    # Vérification de nombre caractère 
    if len(data_scan) == 13:
        return data_scan
    elif len(data_scan) == 30:
        pass
    else:
        pass

