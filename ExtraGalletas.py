# Paloma Argelia Cueto González, a01746765
# Calcular la cantidad de ingredientes que se necesitan para preparar galletas

galletas = int (input ("Numero de galletas: "))

azucar = 1.5/48
mantequilla = 1/48
harina = 2.75/48

azucartotal = galletas*azucar
mantequillatotal = galletas*mantequilla
harinatotal = galletas*harina

print ("Se necesitarán los siguientes ingredientes:")
print ("harina: %.1f" % (harinatotal),"tazas") 
print ("azúcar: %.1f" % (azucartotal),"tazas")
print ("mantequilla: %.1f" % (mantequillatotal),"tazas")