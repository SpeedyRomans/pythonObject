
from numpy import left_shift as lshift,\
    right_shift as rshift,\
    uint32
from numpy.core.fromnumeric import reshape
import serial

#Fonction mise en forme de l' ID pour un filtre
def filterForm (idToConvert) :
    convertedId = int(idToConvert,16)   #Transformation en variable int
    convertedId = lshift(convertedId,5) #Multiplier par 32 ou decaler 5 fois à gauche
    convertedId = convertedId | 31 # mettre les 5 bits de poid faible à 1
    filt = hex(convertedId)[2:] # enlever 0x à la chaine
    filt = filt.rjust(4,'0')       
    return filt.upper()


# Initilisation du port serie
ser = serial.Serial(
    port='COM5',\
    baudrate=57600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

# Fonction ecrire sur le port
def sendOnRS(val):
    if isinstance(val,str):
        ser.write(val.encode('utf-8')) # La variable est envoyée 
        ser.write(chr(13).encode('utf-8')) # Carrier return (chr13) pour fin de ligne

def extractFrame(line):
    if len(line) > 5:
        idNumber= line[1:4] # Identifiant du message
        dataLenthCode= line[4] #  Longueur de la Trame
        frame= line[5:] # Trame du message
        print(idNumber," ",frame)

        if idNumber == "2F7":
            print ("La charge est de ",Weight(frame))
        elif idNumber == "2F8":
            print ("La masse totale est de ",Weight(frame))
        
def Weight(frame):
    result=lshift(int(("0x"+frame[14:16]),base=16),24) # base 2^24 
    result=lshift(int(("0x"+frame[12:14]),base=16),16) + result # base 2^16
    result=lshift(int(("0x"+frame[10:12]),base=16),8) + result # base 2^8
    result=int(("0x"+frame[8:10]),base=16) + result # base 2^0
    return result

# Initialisation 

print("connected to: " + ser.portstr)

# Initialisation CAN 250 kb
sendOnRS('S5')

# filtres 1 et 2 si pas de filtre ACR 000 ACM 7FF

accepCodeRegister = 'M'+ filterForm('000') + filterForm('2F0')
print (accepCodeRegister)
acceptMaskRegister= 'm'+ filterForm('000') + filterForm('F')
print(acceptMaskRegister)

sendOnRS('W0')# Dual filter
sendOnRS(accepCodeRegister)
sendOnRS(acceptMaskRegister)

# Ouverture du port
sendOnRS('O')
print("port ouvert")

line = []
charLine = ""
lineNumber = 0

# Execution du programme Remplacer par while TRUE pour fonctionement continu

while lineNumber < 50 :
    for c in ser.read():
        line.append(c)
        charLine = charLine + chr(c)
        if c == 13 :
            # Traitement des informations
            print (charLine)
            print (line)
            extractFrame(charLine)

            # Remise à 0 des lignes
            line = []
            charLine = ""
            lineNumber = lineNumber +1

# Fermeture du port
sendOnRS('C')
ser.close()
print("Com3 ferme")

