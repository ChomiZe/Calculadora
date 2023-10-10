'CREAR CALCULADORA'
'REQUERIMIENTOS'
'Deberara tener un menu de opciones para seleccionar la operacion'
'Debera solicitar 2 valores por cada operacion'
'Debera funcionar con una sola variable'

print('*************************************************************')
print('♥•••○○○○○♦ CALCULADORA DE UNA SOLA VARIABLE ♦○○○○○•••♥')
print('*************************************************************')

print('***********************************')
print('◘ Menu de Opciones ◘')
print('***********************************')

print('1. SUMA')
print('2. RESTA')
print('3. MULTIPLICACION')
print('4. DIVISION')
print('5. DIVISION ENTERA')
print('6. EXPONENTE')
print('7. MODULO O RESTO \n')

numero = int(input('Introduce la opcion deseada:'))

if numero == 1:
    print('Elegiste suma \n')
    numero = int(input('Introduce el primer nuemro:'))
    numero+= int(input('Introduce el segundo nuemro:'))
    print('El resultado de la suma es:', numero)
elif numero == 2:
    print('Elegiste Resta \n')
    numero = int(input('Introduce el primer nuemro:'))
    numero-= int(input('Introduce el segundo nuemro:'))
    print('El resultado de la resta es:', numero)
elif numero == 3:
    print('Elegiste multiplicacion \n')
    numero = int(input('Introduce el primer nuemro:'))
    numero*= int(input('Introduce el segundo nuemro:'))
    print('El resultado de la multiplicacion es:', numero)
elif numero == 4:
    print('Elegiste division \n')
    numero = float(input('Introduce el primer nuemro:'))
    numero/= float(input('Introduce el segundo nuemro:'))
    print('El resultado de la division es:', round(numero, 2))
elif numero == 5:
    print('Elegiste division entera \n')
    numero = int(input('Introduce el primer nuemro:'))
    numero//= int(input('Introduce el segundo nuemro:'))
    print('El resultado de la division entera es:', numero)
elif numero == 6:
    print('Elegiste exponente \n')
    numero = int(input('Introduce el primer nuemro:'))
    numero**= int(input('Introduce el segundo nuemro:'))
    print('El resultado del exponente es:', numero)
elif numero == 7:
    print('Elegiste Modulo o resto \n')
    numero = int(input('Introduce el primer nuemro:'))
    numero%= int(input('Introduce el segundo nuemro:'))
    print('El resultado del Modulo o resto es:', numero)
else:
    print('La opcion elegida no existe vuelva a intentar')