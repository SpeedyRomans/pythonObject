# 6 t=[25, 47,88, 42, 113]
# Déterminer l'élément max de t
from numpy import random as rdm
t=[25, 47,88, 42, 113]
for i in t:
    maxi = 0
    if i> maxi :
        maxi = i
print ("le maxi est :",maxi)
#Choisir un element au hazard
print ( t[int((rdm.random())*len(t))] )
