print("==========GASOLINERA============")
Dispensadores = float(input("Ingrese la cantidad de dispensadores:\t\t"))
PrecioGasolina = float(input("Ingrese el precio de la gasolina:\t\t"))

GALON = 3.7854
#galon a litros
DispensadoresLitros = Dispensadores * GALON
PrecioPagar = DispensadoresLitros * PrecioGasolina

print("Precio Total a pagar es:\t\t".format(PrecioPagar))