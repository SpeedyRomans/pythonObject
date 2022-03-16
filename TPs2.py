# Écrire un programme qui convertit en degré une
# température fahrenheit, ou l'inverse
# prévoir 2 saisies : une pour le type d'opération, une
# pour la température
# Tf = Tc * 1.8 + 32
# Tc = Tf * 0.55 – 17.78
# Nota : Le chiffre saisi, une chaîne de caractères, doit
# être converti en chiffre entier ou flottant:
# int(chaine_saisie) ou float(chaine_saisie)
temperature = int(input('Rentrez la tempétature'))
unite = input('Rentrez l\'unité de la temperature par défaut Celcius')
if unite == "" or unite[0]=='c':
    print (1.8*float(temperature)+32,"degres fahrenheit")
else :
    print (0.55*float(temperature)-17.78,"degres Celsius")




