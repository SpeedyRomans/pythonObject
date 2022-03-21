# Entrer un mot par ligne
# Compter le nombre d’occurrences de chaque mot
# Classer par ordre alphabétique
# Utiliser le dictionnaire
# Exemple
# Mots entrés Résultats
# kawasaki honda : 1
# moto guzzi kawasaki :2
# honda moto guzzi : 1
# kawasaki

#Création d'un dictionnaire de motos
dicoMoto ={}
marqueMoto=''
while marqueMoto != "q" :
    marqueMoto=input('Marque de moto :')
    #verifier si la clee existe
    if marqueMoto=="q" :
        break
    if dicoMoto.get(marqueMoto)==None:
        dicoMoto[marqueMoto] = 1
    else :
        dicoMoto[marqueMoto] +=1 
print (dicoMoto)
for marqueMoto in sorted(dicoMoto) :
    print( marqueMoto,dicoMoto[marqueMoto])
    