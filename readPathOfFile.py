# import des bibliotheques de la classe
from tkinter import filedialog as fd

# Cette classe recherche une ligne avec une chaine de caractère dans un fichier
class SearchLineWithString:
	def	__init__(self, fileToSearch, stringToFind="(* @PATH"):
		self.fileToSearch = fileToSearch
		self.stringToFind = stringToFind

		# Longeur de la chaine à chercher
		lenOfStrinToFind = len(stringToFind)
		
		with open(fileToSearch, "r") as file:
			# Initialisation de la variable de retour
			self.lineFound = " Rien trouvé "
			for line in file:
				# Insérer içi le code de recherche de chaine de caractère
				if line.find(self.stringToFind) != -1:
					self.lineFound = line
				
			file.close()

# Cette classe recherche une arborescence dans un fichier
class ReadMyPath(SearchLineWithString):

	def __init__(self, fileToSearch):
		SearchLineWithString.__init__(self, fileToSearch=fileToSearch, stringToFind="@PATH")
		
titi = fd.askopenfilename()
toto = ReadMyPath(titi)
print(toto.lineFound)
