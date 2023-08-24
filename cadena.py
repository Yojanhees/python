mensaje = "      Bievenido ... al curso de Python "

# metodo len, imprimen el tamaño de longitud del string
#print("texto original ", mensaje)
#print("El tamaño del texto es de ", len(mensaje))


#  strip, quita espacios de inicio y al final
sinEspacios = mensaje.strip()

#print("El texto sin espacios ", sinEspacios)
#print("El tamaño del texto sin espacios es de ", len(sinEspacios))

#UPPER mayúscula sostenida
#print("texto En MAYUSCULA sostenida")
#print(sinEspacios.upper)

# lower que minuscula
#print("Texto en miúscula sostenida")
#print(sinEspacios.lower())

#tittle inicial de cada palabra en Mayuscula
#print(sinEspacios.title())
#print(sinEspacios.capitalize())

parrafo = sinEspacios.split("...")
print(parrafo[0])
print(parrafo[1])