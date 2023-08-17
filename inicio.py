print("--- Calcular nota definitiva ---")
nombre = input("Nombre estudiante: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
definitiva = (nota1 + nota2 + nota3)/3
print("Nombre: ", nombre, "Nota 1 -->", nota1, "Nota2 -->", nota2, "Nota 3 -->", nota3, "Definitiva -->", definitiva)

""" if definitiva>=3.0:
    print ("El estudiante ", nombre, "tiene una calificación de", definitiva, "por lo tanto aprobó")
else:
    print ("El estudiante ", nombre,"tiene una calificación de", definitiva, "reprobó por vago") """
    
if definitiva >=0 and definitiva <=5: 
    if definitiva <= 2:
        print("El estudiante ", nombre, "Tiene problemas de atención")
        
    elif definitiva < 3:
        print("El estudiante ", nombre, "Puede recuperar")  
    elif definitiva <= 4:
        print("El estudiante ", nombre, "Aprobó, felicidades")
    elif definitiva <= 4.6:
        print("El estudiante ", nombre, "Es genial, excelente nota")  
    elif  definitiva >=4.6:
        print("El estudiante ", nombre, "Felicidades es uno de los mejores estudiantes")
   

 