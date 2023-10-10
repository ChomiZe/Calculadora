"Desarrollar un programa que solicite un numero entero desde teclado"
"este debe determinar si el numero introducido es par o impar"

print("******************************")
print("*Programa que determina si numero es par o impar")
print("******************************")

num_ent = int(input("Ingrese numero entero: "))
if num_ent % 2 == 0:
    print("El numero",num_ent, "es par.")

elif num_ent % 2 == 1:
    print(" El numero",num_ent, "es impar.")

