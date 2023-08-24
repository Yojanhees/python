modulos = ["Logica","Base Datos", "HTML5", "Moviles"]

print(modulos)

#print("Elemento inicial de la lista ", modulos[0])
#print("Elemento final de la lista ", modulos[-1])
#print("numero de elementos que contiene la lista ", len(modulos))
#print("numero de elementos que contiene la lista ", modulos[len(modulos)-1])

#print("Agregar un elemento a lista...Metodoloias agiles ")
modulos.append=("Metodologias agiles")
print(modulos)

modulos.insert(2,"Avanzada")
print(modulos)

# Cantidad de veces que se repite un elemento en la lista
print("Cantidad de veces que aparece HTML5 -->", modulos.count("HTML5"))

print("Lista Ordenada alfabeticamente")
modulos.sort()
#print(modulos)
i=1
for indice in modulos:
    print(indice)
    i=i+1