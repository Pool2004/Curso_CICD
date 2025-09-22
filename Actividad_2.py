import random
# Ejercicio 1: Números pares e impares
# Pide un número al usuario y muestra si es par o impar.
# Luego, imprime todos los números pares hasta ese número.


# SOLUCION
numero = int(input("ingrese el numero"))

if numero % 2 == 0:
    print(f"el numero {numero} es par")
else:
    print("el numero{numero} es inpar")   

print ("numeros pares hasta", numero, ":") 
for i  in range(0, numero + 1, 2):
    print(i)
# -  - - - - -- - - - - - - - - - - - - - - - -- - - - - - - - - - - - -- - - - - -
# Ejercicio 2: Tabla de multiplicar

# Pide un número y muestra su tabla de multiplicar con un for.


# SOLUCION
num = int(input("ingrese el numero"))
i = 0
while i <11:
    print (f"{num} X {i} = {num *i}")
    i +=1
# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -

# Ejercicio 3: Adivina el número

# El programa elige un número secreto (ejemplo: 7) y el usuario debe adivinarlo.
# Usa un while para seguir intentando hasta que acierte.



# SOLUCION
num_secreto = random.randint(1, 10)

intento = None
while intento != num_secreto:
    intento = int(input("ingresa el numero"))

    if intento < num_secreto:
        print("el numero secreto es mayor")
    elif intento > num_secreto:
        print(" el numero secreto es menor")
    else:
        print("felicidades adivinaste el numero")       


# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -

# Ejercicio 4: Calculadora básica

# Pide dos números y una operación (+, -, *, /).
# Usa condicionales para decidir la operación.


# SOLUCION
num1 = int(input("ingrese el primer numero"))
num2 = int(input("ingrese el segundo numero"))

operacion = input("ingrese la operacion(+,-,*,/):")

if operacion == "+":
    resultado = num1 + num2
    print(f"el resultado de {num1} + {num2} es igual: {resultado}")

elif operacion == "-":
    resultado = num1 + num2
    print(f"el resultado de {num1} - {num2} es igual: {resultado}")  

elif operacion == "*":
    resultado = num1 + num2
    print(f"el resultado de {num1} * {num2} es igual: {resultado}")   

elif operacion == "/":
    if num2 != 0:
        resultado = num1 + num2
        print(f"el resultado de {num1} / {num2} es igual: {resultado}")   
    else:
        print("error, no se puede dividir entre cero")         
# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -

# Ejercicio 5: Contador de vocales

# Pide una palabra y cuenta cuántas vocales tiene con un for.


# SOLUCION
vocale = ("a", "e", "i", "o","u")

palabra = input("ingrese una palabra")



# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -
# - - - - --  IMPORTANTE - - - - - -- 

# La solución debe hacerla en su rama respectiva, plazo maximo viernes 19/09/2025 a las 12 PM (Noche)
