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

def re_scan(valeur):
    regex = r"XS\d\d\d\d\d\d\d\d\d"
    # Vérification de la valeur sois une chaine de caractère 
    if isinstance(valeur,str):
        test_str = valeur
    else:
        return False

    matches = re.finditer(regex, test_str, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        
        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            
            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

def scan_verif(data_scan):
    # Vérification de nombre caractère 
    if len(data_scan) == 13:
        return data_scan
    elif len(data_scan) == 30:
        
        
        pass
        
    else:
        pass



if __name__ == '__main__':
    print(re_scan("Ex%0057470XS410656256248848901"))