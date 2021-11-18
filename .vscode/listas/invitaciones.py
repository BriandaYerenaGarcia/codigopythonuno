#Lista de amigos Invitados
lista = []

#4.1 Almacenar nombres en lista 
nombres = ["Mariana", "Manuel", "Rafa", "Oscar", "Alejandro", "Paola", "Jose", "Dani"]

print(f"Amiga {nombres[0]} quiero invitarte a cenar")
print(f"Amigo {nombres[1]} quiero invitarte a cenar")
print(f"Amigo {nombres[2]} quiero invitarte a cenar")
print(f"Amigo {nombres[3]} quiero invitarte a cenar")
print(f"Amigo {nombres[4]} quiero invitarte a cenar")
print(f"Amiga {nombres[5]} quiero invitarte a cenar")
print(f"Amigo {nombres[6]} quiero invitarte a cenar")
print(f"Amigo {nombres[7]} quiero invitarte a cenar")

#4.2 Mensaje sobre el muerto y remplazo del mismo
print(f"{nombres[2]} no podrá asistir porque se murio")

nombres.pop(2)
nombres.insert(2, "Carlos")

print(f"Amigo {nombres[2]} quiero invitarte a cenar")

#4.3 Mesa mas grande y mas invitados 
print("Ahora tengo más espacio y me permitieron invitar a 3 personas más")

nombres.insert(0, "Lupita")
nombres.insert(3, "Edson")
nombres.append("Aldo")



print(f"Amiga {nombres[0]} quiero invitarte a cenar")
print(f"Amiga {nombres[1]} quiero invitarte a cenar")
print(f"Amigo {nombres[2]} quiero invitarte a cenar")
print(f"Amigo {nombres[3]} quiero invitarte a cenar")
print(f"Amigo {nombres[4]} quiero invitarte a cenar")
print(f"Amiga {nombres[5]} quiero invitarte a cenar")
print(f"Amigo {nombres[6]} quiero invitarte a cenar")
print(f"Amiga {nombres[7]} quiero invitarte a cenar")
print(f"Amigo {nombres[8]} quiero invitarte a cenar")
print(f"Amigo {nombres[9]} quiero invitarte a cenar")
print(f"Amigo {nombres[10]} quiero invitarte a cenar")



print(f"Amigo {nombres[0]} siento mucho no poder invitarte a mi fiesta")
nombres.pop(0)
print(f"Amigo {nombres[0]} siento mucho no poder invitarte a mi fiesta")
nombres.pop(0)
print(f"Amigo {nombres[0]} siento mucho no poder invitarte a mi fiesta")
nombres.pop(0)
print(f"Amigo {nombres[0]} siento mucho no poder invitarte a mi fiesta")
nombres.pop(0)
print(f"Amigo {nombres[0]} siento mucho no poder invitarte a mi fiesta")
nombres.pop(0)
print(f"Amigo {nombres[0]} siento mucho no poder invitarte a mi fiesta")
nombres.pop(0)
print(f"Amigo {nombres[0]} siento mucho no poder invitarte a mi fiesta")
nombres.pop(0)
print(f"Amigo {nombres[0]} siento mucho no poder invitarte a mi fiesta")
nombres.pop(0)
print(f"Amigo {nombres[0]} siento mucho no poder invitarte a mi fiesta")
nombres.pop(0)

print(f"Amigo {nombres[0]} gracias por acompañarme en la cena")
print(f"Amigo {nombres[1]} gracias por acompañarme en la cena")


