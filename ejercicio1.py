user = "potasio" 
contra = "holabro"

usuario =input ("Ingrese su nombre de usuario: ")
contraseña =input ("Ingrese su contraseña: ")



if usuario == user and contraseña == contra: 
    print("Haz iniciado sesión. Bienvenido potasio")   
elif usuario == user and contraseña != contra:
    print("Contraseña incorrecta. La contraseña empieza con: " + contra [0])
else:
    print("El usuario no existe :( ") 


