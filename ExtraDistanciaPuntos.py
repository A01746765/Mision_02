# Paloma Argelia Cueto González, A01746765
# Descripción: Calcular la distancia entre dos puntos

x1 = int (input ("x1: "))
y1 = int (input ("y1: "))
x2 = int (input ("x2: "))
y2 = int (input ("y2: "))

import math
distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print ("Distancia: %.3f" % (distancia))