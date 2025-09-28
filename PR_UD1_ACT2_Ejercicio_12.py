#Programa12
lado=input("Introduce el valor del lado de un trapecio isósceles ")
base_menor=input("Introduce el valor del base menor del mismo trapecio isósceles ")
base_mayor=input("Introduce el valor del base mayor del mismo trapecio isósceles ")
altura=input("Introduce el valor del altura del mismo trapecio isósceles ")
perímetro=float(lado)+float(lado)+float(base_menor)+float(base_mayor)
área=float(float(base_menor)+float(base_mayor))/2*float(altura)
print(f"El perímetro del trapecio isósceles és: {perímetro}")
print(f"El área del trapecio isósceles és: {área}")
