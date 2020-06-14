#Estructura repetitiva while
cantidad = 0
x = 1
n = int(input("Cuántas piezas cargará: "))
while x <= n:
	largo = float(input("Ingrese la media de la pieza: "))
	if largo >= 1.2 and largo <= 1.3:
		cantidad = cantidad + 1
	x = x + 1
print("La cantidad de piezas aptas son: ")
print(cantidad)