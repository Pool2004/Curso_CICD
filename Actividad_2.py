# Ejercicio 1: Números pares e impares
# Pide un número al usuario y muestra si es par o impar.
# Luego, imprime todos los números pares hasta ese número.


# SOLUCION

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
print("Números pares hasta", numero, ":")
for i in range(2, numero + 1, 2):
    print(i, end=" ")
print()  # Nueva línea al final

# -  - - - - -- - - - - - - - - - - - - - - - -- - - - - - - - - - - - -- - - - - -
# Ejercicio 2: Tabla de multiplicar

# Pide un número y muestra su tabla de multiplicar con un for.


# SOLUCION

num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -

# Ejercicio 3: Adivina el número

# El programa elige un número secreto (ejemplo: 7) y el usuario debe adivinarlo.
# Usa un while para seguir intentando hasta que acierte.

# SOLUCION

import random
numero_secreto = random.randint(1, 10)
adivina = None
while adivina != numero_secreto:
    adivina = int(input("Adivina el número secreto (entre 1 y 10): "))
    if adivina < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif adivina > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! Adivinaste el número secreto.")


# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -

# Ejercicio 4: Calculadora básica

# Pide dos números y una operación (+, -, *, /).
# Usa condicionales para decidir la operación.


# SOLUCION

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")
if operacion == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Error: División por cero no es permitida.")
else:
    print("Operación no válida.")


# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -

# Ejercicio 5: Contador de vocales

# Pide una palabra y cuenta cuántas vocales tiene con un for.


# SOLUCION

palabra = input("Ingrese una palabra: ")
vocales = "aeiouAEIOU"
contador = 0
for letra in palabra:
    if letra in vocales:
        contador += 1
print(f"La palabra '{palabra}' tiene {contador} vocales.")  


# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -
# - - - - --  IMPORTANTE - - - - - -- 

# La solución debe hacerla en su rama respectiva, plazo maximo viernes 19/09/2025 a las 12 PM (Noche)
