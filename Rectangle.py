
#  appel des Bibliotheques utile à la classe

from numpy import sqrt as racine

#'Programation de la classe'
class rectangle:
    # Affectation des variables d'entrée 
    longueur = 3
    largeur =4

    def calculate_area(self):
        return self.largeur * self.longueur
    def calculate_diagonale(self):
        diagonale= racine(self.largeur^2 +self.longueur^2)
        return diagonale
    def calculate_perimeter(self):
        return 2*(self.largeur + self.longueur)

    

