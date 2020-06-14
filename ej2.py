sueldo = int(input("Introduce el sueldo: "))

if sueldo > 3000:
	print("El usuario debe pagar el porcentaje de impuestos.")
if sueldo <= 3000:
	print("El usuario esta exento de pagar impuestos.")

if sueldo > 6000 and sueldo < 10000:
	print("El usuario debe pagar una bonificacion de 1000 euros.")
if sueldo == 20000 or sueldo == 30000:
	print("El usuario paga un 10 por ciento de su saldo.")
