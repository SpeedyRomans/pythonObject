# 20 premiers termes de la table de 20
i=1
tableDe=7
while i<=20 :
    if i%3==0 :
        car = '*'
    else :
        car = ''
    print(tableDe,'*',i,'=',tableDe*i,car )
    i=i+1