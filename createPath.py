#!/usr/bin/python3
import os
from tkinter import filedialog

# start editable vars #
pathsep		= chr(92)			# path seperator ('/' for linux, '\' or chr(92) for Windows)
exclude		= ['Thumbs.db','.tmp']	# exclude files containing these strings

# Cette fonction recherche une ligne avec une chaine de caractère dans un fichier
def SearchLineWithString(fileToSearch,stringToFind):
	with open(fileToSearch, "r") as file:
		# Initialisation de la variable de retour
		lineFound = ""
		for line in file:
			# Insérer içi le code de recherche de chaine de caractère
			if line.find(stringToFind) != -1:
				lineFound = line.removeprefix(stringToFind)
				break
		file.close()
	return lineFound

def lineToPath(line):
	# Mise en forme de la ligne
	pathFound = line.replace("'","")
	pathFound = pathFound.replace(":= ","")
	pathFound = pathFound.replace(" *)","")
	pathFound = pathFound.replace(" ","")
	pathFound = pathFound.strip()
	return pathFound


# Choix du dossier source
folder = filedialog.askdirectory()

# Parcour du dossier 
for path,dirs,files in os.walk(folder):
	for fn in sorted(files):
		if not any(x in fn for x in exclude):
			# Nom du fichier trouvé
			originFileName = (folder+"/"+fn)

			#Recherhe son arboresence dans le fichier trouvé
			line = SearchLineWithString(originFileName,"(* @PATH")
			pathFound = lineToPath(line)

			# non de la destination du fichier trouvé
			repertory = folder+pathFound
			destFileName= repertory+"/"+fn

			# Creation de l'arborescence et transfert du fichier
			#print(destFileName)
			os.makedirs(repertory, exist_ok=True)
			os.replace(originFileName,destFileName)
