#Fonction qui prend en para une chaîne de caractères et
#retourne une liste contenant les mots de la chaîne;
#délimiteurs de mots : esp . , ;

def maFonction(chaine,separateur):
    result=chaine.replace(separateur,' ')
    return result.split()
    
print(maFonction('abcdef!ghijklm!no+pqrs!tuvwxyzabc',"!"))
