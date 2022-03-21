import random
from types import NoneType

class Jeu():
    '''
    Définir la classe Jeu() → instancie un jeu de cartes composé de 52 cartes
chaque carte est représenté par un tuple de 2 éléments :
n° de la carte (2 – 14) et n° de couleur (1 – 4)
 méthode __init__ : création d'une liste de 52 tuples
 méthode nom_carte : retourne le nom d'une carte
ex : nom_carte(14,3) → As de Trèfle
 méthode battre() : sert à randomiser le jeu de carte
se servir de la fonction shuffle du module random
c.f. du TP4_11.py, fonction ramdom.shuffle(c )
 méthode tirer() : retourne la 1ère carte de la liste : S'il n'en
reste plus, retourner la constante spéciale None
    
    '''
    couleurs =(None,'coeur','carreau','pique','trefle')
    valeurs = (None,None,'deux','trois','quatre','cinq','six','sept','huit',\
        'neuf','dix','valet','dame','roi','as')

    def __init__(self): # fonction d'initialisation
        self.cartes =[]
        for i in range(1,len(Jeu.couleurs)):
            for j in range(2,len(Jeu.valeurs)):
                self.cartes.append([i,j])
       
    # methode nom_carte
    def nom_carte(self,couleur,valeur) :
        return Jeu.valeurs[valeur]+' de '+Jeu.couleurs[couleur]
    
    # methode battre
    def battre(self):
        random.shuffle(self.cartes)

    # methode tirer
    def tirer(self):
        if self.cartes != []:
            return self.cartes.pop()
        else: return None





jeu1 =Jeu()
print (jeu1.nom_carte(2,13))
jeu1.battre()
print (jeu1.cartes)
carteTirée= jeu1.tirer()
print (jeu1.nom_carte(carteTirée[0],carteTirée[1]))


