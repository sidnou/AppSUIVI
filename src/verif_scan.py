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

- Vérification données scanné ne sois pas en doublon 
    

'''

def re_scan(valeur,long_valeur): 
    if long_valeur >= 30:
        regex = r"XS\d{9}"
        matches = re.finditer(regex, valeur, re.MULTILINE)
        for match in matches:
            return match[0]+"FR"
    else:
        return False
       
def scan_verif(data_scan):
    # Vérification de la valeur sois une chaine de caractère 
    if isinstance(data_scan,str):
        # Vérification de nombre caractère 
        if len(data_scan) == 13:
            return data_scan
        elif len(data_scan) >= 30:
            return re_scan(data_scan,len(data_scan))
        # si data_scan est inférieur a 13
        else:
            return False
        # si data_scan n'est pas string
    else:
        return False



if __name__ == '__main__':
    print(scan_verif("Ex%0057470XS410656256248848901"))
    print(scan_verif("Ex%005747XS41065625648848901")) # Valeur fausse 
    print(scan_verif("[)>01020057470901848XS410656256248GEOP5357250321/1.5KGN115 Rue des RomainsHOMBOURG HAUTEpicerie La Chapelle07G03000HILLEBRAND Joris0663667039joris.hillebrand4@gmail.com1.5KGM67S-2601-00292M67S-2601-00292N007S010Maintronic/OCI03902279402 Rue Andre Marie AmpereMundolsheim6745025007D001011210126XS410656256FR00000M67S-2601-   ]"))
    print(scan_verif(256532566266545665855)) # Valeur fausse 
