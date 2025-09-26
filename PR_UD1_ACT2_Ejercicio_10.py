#Programa10
var1=input("Introduce el primer número ")
var2=input("Introduce el segundo número ")
cociente=float(var1)/float(var2)
resto=float(var1)%float(var2)
print(f"El cociente és: {cociente}")
print(f"El resto és: {resto}")
if resto % 2 == 0:
    print(f"El dividendo es par.")
else:
    print(f"El dividendo es impar.")