#programa para calucular el are de un cuadrado 

lado = input ("Ingresa el valor del lado: ")


#Convertimos un string a un entero int 
lado = int(lado)

#area = lado * lado 

area = lado ** 2


#f es una cadena para usar lado y area como variable y no como texto 
print(f"El area del cuadrado con l={lado} es: {area}")