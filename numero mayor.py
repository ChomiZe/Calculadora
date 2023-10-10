"Desarrollar un programa que solicite 3 numeros enteros desde teclado"
"Posteriormente debera determinar atraves de un mensaje en pantalla cual es el numero mas grande"

print("*********************************************************************")
print("Programa para determinar Cual es el numero mas grande de tres numeros")
print("*********************************************************************")

nu1 = int(input("Ingrese Primer numero: "))
nu2 = int(input("Ingrese Primer numero: "))
nu3 = int(input("Ingrese Primer numero: "))

if nu1 > nu2 and nu1 > nu3:
    print("El numero ", nu1, " es el numero mas grande de los tres")
else:
    if nu2 > nu3:
        print("El numero ", nu2, " es el numero mas grande de los tres")
    else:
        print("El numero ", nu3, " es el numero mas grande de los tres")