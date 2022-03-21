# Programme qui demande à un utilisateur son
# nom, prénom, rue, ville CP et range ces données dans
# un fichier
# Chaque enregistrement tient sur une ligne et chaque
# champ est séparé du suivant par un #

# Création d'un dictionaire personel

from telnetlib import theNULL


donnes=['nom','prenom','rue','ville','CP',]
# ouverture du fichier
fh=open('fichier.txt','w' )
while True :
    ligne=""
    for champ in donnes :
        donne = input (champ)
        if donne =='q' : break
        if ligne=='':
            ligne=donne
        else:
            ligne=ligne+'#'+donne
    # Pour sortir de la boucle infinie
    if donne =='q' : break
    # ajouter une ligne 
    print (ligne,file=fh)
# fermeture du fichier
fh.close()

    
    
