# A l'aide d'une fonction prenant en argument une
# chaîne et une longueur de sous-chaine, réaliser une
# chaîne à partir de ces sous-chaînes dans l'ordre
# inverse de leur apparition
# Exemple
# MaFonction(abcdefghijklmnopqrstuvw, 5)
# Résultat uvwpqrstklmnofghijabcde

def maFonction(chaine,longSousChaine):
    index =0
    liste =[]
    while index < len(chaine):
        liste.append(chaine[index:index+longSousChaine])
        index+=longSousChaine
    liste.reverse()    
    return (liste)

print(maFonction('abcdefghijklmnopqrstuvwxyzabc',4))
