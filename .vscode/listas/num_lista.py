lista = []

#6.1 Crear una lista del 0-10 
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Invertir usando while 
posicion = len(numeros)-1 


numeros2 = []

while (posicion >= 0):
    numeros2.append(numeros[posicion])
    posicion = posicion - 1
    
print(numeros2)

