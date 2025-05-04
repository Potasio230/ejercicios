#Ejercicio 2: Constantes y Calculadora de Descuentos


#definimos los porcentajes de descuento
descuentoEstudiante = 0.15 #ufff
descuentoClienteFrecuente = 0.10 #nada mal
descuentoIndividuoNormal = 0.00 #jaja no tiene descuento

#creamos variables para el cálculo
descuento = 0.0
precioNuevo = 0.0

#precios de los artículos disponibles en la tienda
PoleronRojo = 12000
CamisaAzul = 8500
ParDeCalcetinesVerdes = 3000
GorraNegra = 6500

#mostramos los artículos disponibles
print("Artículos disponibles: ") 
print("PoleronRojo:           12000~~~ CamisaAzul: 8500") 
print("ParDeCalcetinesVerdes: 3000~~~ GorraNegra: 6500")
precioOriginal = float(input ("Ingrese el precio del artículo que desea comprar: "))

#preguntamos qué tipo de cliente es y se calcula según el tipo
print("¿Es usted estudiante? o ¿Es usted cliente frecuente? o ¿Es usted un individuo normal?")
#es estudiante
opcion = input("Elija una opcion (1-3): ")
if opcion == "1":
    descuento = (precioOriginal * descuentoEstudiante)
    precioNuevo = precioOriginal - descuento
    print(f"Descuento de estudiante aplicado {descuento}")
#es frecuente
elif opcion == "2":
    descuento = (precioOriginal * descuentoClienteFrecuente)
    precioNuevo = precioOriginal - descuento
    print(f"Descuento de cliente frecuente aplicado {descuentoClienteFrecuente}")
#normal
elif opcion == "3":
    descuento = descuentoIndividuoNormal
    print("Descuento... espera, no hay descuentos para tí...")
else:
    print("No eres nada, al parecer...")

#mostramos el resumen de la compra
print("Resumen de la compra")
print(f"Precio original del producto: {precioOriginal}")
print(f"El precio final del producto con descuento es: {precioNuevo}")



