#5.Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “1234” se indica “Has entrado al sistema”,
#sino se da un error.

usuSecreto = "pepe"
passSecreto = "1234"

usuario = input("Dime tu usuario: \n")
password = input("Dime tu contraseña: \n")


while (usuario!=usuSecreto or passSecreto!=password):   #en el momento que uno sea incorrecto, da error, con "or"

    if(usuSecreto!=usuario):
        print ("Error en el usuario")
        usuario = input("Dime tu usuario: \n")

    elif (passSecreto!=password):
        print ("Error en la contraseña")
        password = input("Dime tu contraseña: \n")

print ("Has entrado al sistema")