# import des bibliotheques de la classe
from tkinter import filedialog as fd


# Cette classe recherche une ligne avec une chaine de caractère dans un fichier
class SearchLineWithString:
	def	__init__(self, fileToSearch, stringToFind="(* @PATH"):
		self.fileToSearch = fileToSearch
		self.stringToFind = stringToFind
		# Ouverture du fichier scruté
		with open(fileToSearch,"r") as file:
			# Lecture de toutes les ligne du fichier			
			for line in file:
				if line.find(stringToFind) != -1:
					# Ligne trouvée
					return line
					# Fin de la recherche
					break
			return ""
			file.close()

# Cette classe recherche une arborescence dans un fichier
class ReadMyPath(SearchLineWithString):

	def __init__(self, fileToSearch):
		SearchLineWithString.__init__(self, fileToSearch=fileToSearch, stringToFind="@PATH")
		
titi = fd.askopenfilename()
toto = ReadMyPath(titi)
print(toto.path)


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
				lineFound = lineFound.replace("'","")
				lineFound = lineFound.replace(":= ","")
				lineFound = lineFound.replace(" *)","")
				lineFound = lineFound.replace(" ","")
				lineFound = lineFound.strip()
		file.close()
	return lineFound	

# Choix du dossier source
folder = filedialog.askdirectory()
print(folder)

# Parcour du dossier 
for path,dirs,files in os.walk(folder):
	for fn in sorted(files):
		if not any(x in fn for x in exclude):
			# Nom du fichier trouvé
			originFileName = (folder+"/"+fn)

			#Recherhe son arboresence dans le fichier trouvé
			pathfound = SearchLineWithString(originFileName,"(* @PATH")

			# non de la destination du fichier trouvé
			repertory = folder+pathfound
			destFileName= repertory+"/"+fn

			# Creation de l'arborescence et transfert du fichier
			#print(destFileName)
			os.makedirs(repertory, exist_ok=True)
			os.replace(originFileName,destFileName)
