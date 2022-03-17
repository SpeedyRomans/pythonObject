# Créer une comprehension list des premiers
# carrées à partir des chiffres impaires <100

print([(nombre**2) for nombre in range(100) if nombre % 2 != 0])
