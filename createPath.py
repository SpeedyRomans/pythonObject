#!/usr/bin/python3
import os
from tkinter import filedialog

# start editable vars #
pathsep		= chr(92)			# path seperator ('/' for linux, '\' or chr(92) for Windows)
# outputfile	= "L://FAUN//BE//2.Logiciel//FCS//Projets//FNCOM//Family V03//APPL_CM_V03_01_02_xxxx//inventory.txt" # file to save the results to
# folder = "L://FAUN//BE//2.Logiciel//FCS//Projets//FNCOM//Family V03//APPL_CM_V03_01_02_xxxx//SourceCode//"
exclude		= ['Thumbs.db','.tmp']	# exclude files containing these strings
# end editable vars #

# Choix du dossier source
folder = filedialog.askdirectory()
# Nom du fichier
outputfile	=filedialog.asksaveasfilename()
print(folder)
print(outputfile)

# Création ou ouverture du fichier 
with open(outputfile, "w") as txtfile:
	dirList = os.walk(folder)
	print(dirList)
	for path,dirs,files in os.walk(folder):
		#sep = ("\n---------- " + path.split(pathsep)[len(path.split(pathsep))-1] + " ----------")
		#print (sep)
		#txtfile.write("%s\n" % sep)

		for fn in sorted(files):
			if not any(x in fn for x in exclude):
				filename = os.path.splitext(fn)[0]
				extens = os.path.splitext(fn)[1]
				fileFullName = (filename+ extens)
				print (fileFullName)
				txtfile.write("%s\n" % fileFullName )

txtfile.close()