#programa que pida valor en centigrados y lo muestre en farenheit 

centigrados = input ("Ingresa tu temperatura en grados Centigrados")

centigrados = float(centigrados)

farenheit = (centigrados * 9/5) + 32


print(f"La siguiente temperatura en grados centigrados {centigrados} es igual a {farenheit} en grados Fahrenheit")