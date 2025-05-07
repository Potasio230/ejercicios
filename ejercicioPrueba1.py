dinero = 0
bono = 0
print("Menú de decil: ")
print("1. Primer decil")
print("2. Segundo decil")
print("3. Tercer decil")
print("4. Cuarto decil")
print("5. Quinto decil")
print("6. Sexto decil")
print("7. Septimo decil")
print("8. Octavo decil")
print("9. Noveno decil")
print("10. Decimo decil")
print("************************************************")

decil =  int(input("Ingrese el decil (1 - 10): "))

promedio = float(input("Ingrese su promedio final: "))

if promedio > 6.5 and (decil == 1 or decil == 2):
    print("A usted le corresponden $200.000 de la beca")
    dinero = 200000

elif promedio > 6.5 and (decil == 3 or decil == 4):
    print("A usted le corresponden $150.000 de la beca")
    dinero = 150000

elif (promedio > 5.5 and promedio <= 6.5) and (decil == 1 or decil == 2):
    print("A usted le corresponden $120.000 de la beca")
    dinero = 120000

elif (promedio > 5.5 and promedio <= 6.5) and (decil == 3 or decil == 4):
    print("A usted le corresponden $100.000 de la beca")
    dinero = 100000

else:
    print("Error")

if (decil == 1 or decil == 2 or decil == 3):
    bono = + 50000
    if  promedio >= 6.0:
        bono = bono + 30000
        
print("Gracias")
print("Su monto total es: ")
print(dinero + bono)


