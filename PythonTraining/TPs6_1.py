# Définir une classe Domino() qui instancie un domino : 2 faces,
# chaque face a une valeur 0 → 6
# 2 méthodes :
#  aff() qui affiche les 2 valeurs d'un domino
#  somme() qui retourne la somme de ces 2 valeurs
#  si les valeurs d'init sont erronées retourner un domino avec -1 .-1

class Domino():
    def __init__(self, carre1=0, carre2=0): # fonction d'initialisation
        if carre1 <=6 and carre1 >=0 :
            self.carre1 = carre1
        else :
             self.carre1 = -1
        if carre2 <=6 and carre2 >=0 :
            self.carre2 = carre2
        else :
             self.carre2 = -1
         
    # l'objet courant
    def aff(self) :
        print ('carré 1 =', self.carre1, ', carré 2 =', self.carre2)

    def somme(self):
        print ("somme des carrés =", self.carre1+self.carre2 )   

dom1=Domino(7,1)
dom1.aff()
dom1.somme()
