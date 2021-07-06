
#  appel des Bibliotheques utile à la classe
from numpy import sqrt as racine

#'Programation de la classe'
class Rectangle:
    # Affectation des variables d'entrée avec la methode magique
    def __init__(self,longueur, largeur, surface, diagonale, perimetre):
        self.longueur = longueur
        self.largeur = largeur
        self.surface = surface
        self.diagonale = diagonale
        self.perimetre = perimetre

    def calculate_area(self):
        return self.largeur * self.longueur
    def calculate_diagonale(self):
        diagonale= racine(self.largeur^2 +self.longueur^2)
        return diagonale
    def calculate_perimeter(self):
        return 2*(self.largeur + self.longueur)


    

