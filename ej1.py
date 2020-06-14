print ("Datos de la primera persona.")
#input para cargar datos
nombre1 = input("Ingrese nombre de producto: ")
precio1 = int(input("Ingrese un precio: "))
nombre2 = input("Ingrese nombre de producto: ")
precio2 = int(input("Ingrese un precio: "))

bonificacion = 20

precio_compra_total = precio1 + precio2

comparar = precio1 >= precio2
logico = (precio1 < precio2 and precio1 == precio2)

cabecera = "Resultado del producto {0}. y del pruducto. {1}:"

print (cabecera.format(nombre1, nombre2))
print ("El precio del primer valor es mayor o igual al precio del segundo valor: ")
print (comparar)

print("La suma de los dos productos es: " + str(precio_compra_total))
print ("precio1 < precio2 and precio1 == precio2")
print(logico)

precio_compra_total += bonificacion
print("Al precio total le incrementamos su valor que tiene la constante: " + str(precio_compra_total))
