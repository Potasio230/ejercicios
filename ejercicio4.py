#Ejercicio 4: Aritmética y Conversor de Unidades

#mostramos el menú principal
print("Menú de conversores")
print("1. Convertir kilómetros a Millas")
print("2. Convertir millas a Kilómetros")
print("3. Convertir celsius a Fahrenheit")
print("4. Convertir fahrenheit a Celsius")
print("5. Salir")

#pedimos al usuario que elija una opción
opcion = int(input("Seleccione una opción ( 1 - 4 ): "))

#opcion 1
if opcion == 1:
    valor = float(input("Ingrese la distancia en kilómetros: "))
    if valor < 0:
        print("Error: La distancia no puede ser negativa.")
    else:
        millas = valor * 0.621371
        print(f"{valor} km = {millas:.2f} millas")

#opción 2
elif opcion == 2:
    valor = float(input("Ingrese la distancia en millas: "))
    if valor < 0:
        print("Error: La distancia no puede ser negativa.")
    else:
        km = valor / 0.621371
        print(f"{valor} millas = {km:.2f} km")
#opcion 3
elif opcion == 3:
    valor = float(input("Ingrese la temperatura en °C: "))
    fahrenheit = valor * 9/5 + 32
    print(f"{valor}°C = {fahrenheit:.1f}°F")
    
    if valor < 0:
        print("Está bajo cero.")
    elif 15 <= valor <= 25:
        print("Temperatura ambiente.")
    else:
        print("Hace calor.")
#opcion 4
elif opcion == 4:
    valor = float(input("Ingrese la temperatura en °F: "))
    celsius = (valor - 32) * 5/9
    print(f"{valor}°F = {celsius:.1f}°C")

    if celsius < 0:
        print("Está bajo cero.")
    elif 15 <= celsius <= 25:
        print("Temperatura ambiente.")
    else:
        print("Hace calor.")
#opcion 5
elif opcion == 5:   
    print("Saliendo del programa...")

#si elige una opcion erronea
else:
    print("Opción no válida. Seleccione una opción válida: ( 1 - 5)")