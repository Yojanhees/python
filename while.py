respuesta = 1

while respuesta ==1:
    respuesta = int (input("1. Si\n2. No\nEscriba el nro para continuar"))
    while respuesta != 1 and respuesta != 2:
        print("usted dgitó mal 🤦‍♂️")
        respuesta = int (input("1. Si\n2. No\nEscriba el nro para continuar"))