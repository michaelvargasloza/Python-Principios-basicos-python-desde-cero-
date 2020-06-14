#Estructura repetitiva while
x = 1
suma = 0
while x <= 10:
	valor = int(input("Ingrese un valor: "))
	suma = suma + valor
	x = x + 1
promedio = suma / 10
print("La suma de los 10 valores es: ")
print(suma)
print("El promedio es: ")
print(promedio)