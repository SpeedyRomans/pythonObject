# Fonction fibonacci
# f(n)= f(n-1) + f(n-2) f(1) = 0, f(2) = 1
# a) écrire une fonction fibonacci non récursive
# b) écrire une fonction fibonacci récursive
# Comparer la différence de temps de traitement en
# augmentant n : 10, 20, 30 ...
# Utiliser la fonction time() du module time
# import time
# ......
# t=time.time()

def fibonacci(n):
    if n==1 : return 0
    if n==2 : return 1

    return fibonacci(n-1)+fibonacci(n-2)
        
print (fibonacci(5))
