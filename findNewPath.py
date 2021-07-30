class FindNewPath:
    #Appel des bibliothèques
    import numpy

    # Affectation des variables d'entrée avec la methode magique
    def __init__(self,longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
     
    def calculate_area(self):
        return self.largeur * self.longueur
    def calculate_diagonale(self):
        diagonale= numpy.sqrt(self.largeur**2 +self.longueur**2)
        return diagonale
    def calculate_perimeter(self):
        return 2*(self.largeur + self.longueur)


    