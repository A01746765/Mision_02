# Autor: Paloma Argelia Cueto González, A01746765
# Descripcion: Calcular el total de alumnos inscritos y el porcentaje
# de hombres y mujeres.

mujeres = int (input("Mujeres inscritas: "))
hombres = int (input ("Hombres inscritos: "))

total = hombres + mujeres

pmujeres = (mujeres/total)*100
phombres = (hombres/total)*100

print ("Total de inscritos: ", total)
print ("Porcentaje de mujeres: %.1f" % (pmujeres),"%")
print ("Porcentaje de hombres: %.1f " % (phombres),"%")