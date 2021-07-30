#Programme pour utiliser la classe Rectangle

import Rectangle
#L'instance du rectangle de cote 4 et 3 s'appelle r
r = Rectangle.Rectangle(4,3)

area=r.calculate_area()
print("La surface est de ",area)
print ("La diagonale mesure ",r.calculate_diagonale())
print("Le perimetre mesure ", r.calculate_perimeter())




