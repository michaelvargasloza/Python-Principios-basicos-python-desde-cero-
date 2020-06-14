lista = []
for k in range(10):
	lista.append(input("Introduce valor en lista: "))

print ("Los elementos de la lista son: " + str(lista))
valor = int(input("Introduce el valor a modificar de la lista por el índice: "))
nuevo = input("Introduce el nuevo valor: ")
lista[valor] = nuevo
print ("Los elementos de la lista son: " + str(lista))
valor = int(input("Introduce el indice en el que se insertará el nuevo valor: "))
nuevo = input("Introduce el nuevo valor: ")
lista.insert(valor, nuevo)
print ("Los elementos de la lista son: " + str(lista))
nuevo = input("Introduce el valor a eliminar: ")
lista.remove(nuevo)
print ("Los elementos de la lista son: " + str(lista))
nuevo = input("Introduce el valor a buscar: ")
resultado = (nuevo in lista)
if (resultado):
	print ("Existe este elemento y su índice es: " + str(lista.index(nuevo)))
else:
	print ("No existe elemento.")