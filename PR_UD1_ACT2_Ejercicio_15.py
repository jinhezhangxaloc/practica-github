#Programa15
radio=input("Introduce el valor de radio de un cilindro ")
altura=input("Introduce el valor de altura de un cilindro ")
área=float(radio)*float(radio)*3.14*2+float(altura)*float(radio)*3.14*2
volumen=float(radio)*float(radio)*3.14*float(altura)
print(f"El área del cilindro és: {área}")
print(f"El volumen del cilindro és: {volumen }")
