#Ejercicio 3: Operadores y Verificador de Playlist

#se solicitan los datos necesarios
duracion = float(input("¿Cuanto quieres que dure la canción? "))
genero = (input("¿Qué género musical prefieres? "))
añoLanzamiento = int(input("¿Qué año de lanzamiento prefieres? "))

#verificamos si se cumplen los criterios
duracionAdecuada = 2.5 <= duracion <= 4.5
generosPermitidos = genero in ["rock", "pop", "indie"]
añoMinimo = añoLanzamiento > 2010


#si cumple
if duracionAdecuada and generosPermitidos:
    print("¡La canción es perfecta para tu playlist!")
#si no cumple
else: 
    print("La canción no cumple con todos los criterios para la playlist:")
#se explica por qué no cumple cada criterio
    if not duracionAdecuada:
        print(f"La duración ({duracion} min) está fuera del rango ideal (de 2.5 a 4.5 min).")
    if not generosPermitidos:
        print(f"El género '{genero}' no está entre los generos predefinidos (rock, pop o indie).")
    if not añoMinimo:
        print(f"- El año ingresado: {añoLanzamiento} es anterior a 2010.")
    