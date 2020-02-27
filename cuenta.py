# Autor: Paloma Argelia Cueto González, a01746765
# Descripcion: Calcular la propina y el IVA de una cuenta de comida
# al igual que el total a pagar

comida = int (input ("Costo de su comida: "))

propina = comida*.13
IVA = comida*.16

total = propina + comida + IVA

print ("Propina: $ %.2f" % (propina))
print ("IVA: $ %.2f" % (IVA))
print ("Total a pagar: $ %.2f" % (total))
