# Définir une classe CompteBancaire avec deux propriétés
# d'instance nom et solde,avec les valeurs par défaut Dupont et
# 1000. Définir les méthodes
# retrait(somme), depot(somme), consulter().
# autoriser un découvert max de 500
# Exemples d'utilisation
# compte1 = CompteBancaire('Hugo', 1025)
# compte1.depot(550)
# compte1.retrait(325)
# compte1.consulter()
# Votre compte est créditeur de 1250 €
# compte1.retrait(2000)
# Découvert max dépassé. Retrait de 2000 non autorisé
class CompteBancaire():
    def __init__(self, nom='Dupont', solde=1000): # fonction d'initialisation
         self.nom = nom
         self.solde = solde
         
    # methode retrait
    def retrait(self,retrait) :
        if self.solde-retrait > -500:
            self.solde -= retrait
            print (self.nom, "votre nouveau solde est de :", self.solde)
        else :
            print (self.nom, "retrait non autorisé :")

   # methode depot
    def depot(self,depot) :
        self.solde += depot
        print (self.nom, "votre nouveau solde est de :", self.solde)

   # methode consultation
    def consult(self) :
        print (self.nom, "votre solde est de :", self.solde)



cmpPascal=CompteBancaire('Pascal',2000)
cmpAlain=CompteBancaire('Alain',2900)

cmpPascal.retrait(5000)
cmpAlain.consult()
cmpPascal.depot(2500)
