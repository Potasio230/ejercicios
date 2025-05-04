#Ejercicio 1: Variables y Validación de Acceso

#definimos los datos válidos para iniciar sesión
user = "potasio" 
contra = "holabro"

#pedimos al usuario que ingrese su nombre de usuario y contraseña
usuario =input ("Ingrese su nombre de usuario: ")
contraseña =input ("Ingrese su contraseña: ")


#verificamos si el nombre de usuario y la contraseña son correctos
if usuario == user and contraseña == contra: 
    print("Haz iniciado sesión. Bienvenido potasio")   

#si el nombre de usuario es correcto pero la contraseña no, damos una pequeña pista    
elif usuario == user and contraseña != contra:
    print("Contraseña incorrecta. La contraseña empieza con: " + contra [0])

#si el nombre de usuario no es correcto, mostramos un mensaje de error    
else:
    print("El usuario no existe :( ") 


