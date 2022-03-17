# Fonction qui prend en entrée 1 chiffre en paramètre
# d'appel.
# S'il est compris entre 0 et 9 alors retourner le chiffre
# correspondant en lettre.
# Si le chiffre n'existe pas retourner le chiffre sous sa
# forme d'origine (numérique).
# Nota : pour convertir un chiffre en string utiliser la
# fonction str() et un string en chiffre int() ou float()
def convert(valeur):
    chiffre = ['zéro','un','deux','trois','quatre','cinq','six','sept','huit','neuf']
    if valeur < 10:
        lit = chiffre[valeur]
    else:
        lit = str(valeur)
    return (lit)

def add (val1,val2):
    resultat= convert(val1) + " + " + convert(val2)+ "=" + convert(val1+val2)
    return resultat

print(add(5,5))
