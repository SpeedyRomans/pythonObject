# Programme qui reprend le fichier obtenu dans le TP
# précédent, et qui affiche chaque enregistrement,
# demande le sexe et la date de naissance et l'ajoute en
# fin de chaque enregistrement, et met à jour le fichier
# NB : pour retirer l'éventuel retour chariot d'une
# chaîne str → str.rstrip('\n')

donnes=['nom','prenom','rue','ville','CP',]
# ouverture du fichier
fh=open('fichier.txt','r' )
fhN=open('fichier.txt','w' )
for line in fh :
    print (line)
    sexe = input("quel sexe ?")
    birthday = input ("quel est la date de naissance")
    line=line.rstrip()+"#"+sexe+"#"+birthday
    print (line,file=fhN)

    # ajouter une ligne 
# fermeture du fichier
fh.close()
fhN.close()


    
    
