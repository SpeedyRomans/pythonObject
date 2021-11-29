
from numpy import left_shift as lshift,\
    right_shift as rshift,\
    uint32
import serial

#Fonction mise en forme de l' D pour un filtre
def filterForm (idToConvert) :
    convertedId = int(idToConvert,16)   #Transformation en variable int
    convertedId = lshift(convertedId,5) #Multiplier par 32 ou decaler 5 fois à gauche
    return convertedId | 31             # mettre les 5 bits de poid faible à 1

# Fonction dual filter 
def dualFilter(idFrom,idTo):
    #Creation d'un mot de 32 bits 
    idDint = uint32(lshift(filterForm(idFrom),16))
    return idDint | filterForm(idTo)




print(hex(dualFilter('30','30')))
print(hex(dualFilter('2f7','2f7')))



