# import des bibliotheques de la classe
from tkinter import filedialog as fd

fileToSearch = "L:\FAUN\BE\2.Logiciel\FCS\Projets\FNCOM\Family Test\Pascal\APPL_CM_V03_01_02_xxxx\SourceCode\AI_CONV_VALUE.EXP"
# Cette classe recherche une ligne avec une chaine de caractère dans un fichier
class SearchLineWithString:
	def	__init__(self, fileToSearch, stringToFind="(* @PATH"):
		self.fileToSearch = fileToSearch
		self.stringToFind = stringToFind

		# Longeur de la chaine à chercher
		lenOfStrinToFind = len(stringToFind)
		
		with open(fileToSearch, "r") as file:
			for line in file:
				print(len(line)," ",line)

				# Insérer içi le code de recherche de chaine de caractère

				self.path = "Resultat de la recherche"

			file.close()

# Cette classe recherche une arborescence dans un fichier
class ReadMyPath(SearchLineWithString):

	def __init__(self, fileToSearch):
		SearchLineWithString.__init__(self, fileToSearch=fileToSearch, stringToFind="@PATH")
		
titi = fd.askopenfilename()
toto = ReadMyPath(titi)
print(toto.path)