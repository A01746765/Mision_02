# Autor: Paloma Argelia Cueto Gonzalez, a01746765
# Descripcion: Calcular la distancia y el tiempo de un auto con valores determinados.

velocidad = int (input ("Velocidad del auto en km/hr: "))

distancia1 = velocidad*6
distancia2 = velocidad*3.5
tiempo = 485/velocidad

print ("Distancia recorrida en 6 hrs: ", distancia1)
print ("Distancia recorrida en 3.5 hrs: %.1f" % (distancia2))
print ("Tiempo para recorrer 485 km: %.1f" % (tiempo))