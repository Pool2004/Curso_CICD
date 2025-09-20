# Ejercicio 1: Números pares e impares
# Pide un número al usuario y muestra si es par o impar.
# Luego, imprime todos los números pares hasta ese número.


# SOLUCION
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")
print("Números pares hasta", num, ":")
for i in range(2, num + 1, 2):
    print(i, end=" ")
print() 

# Ejercicio 2: Tabla de multiplicar

# Pide un número y muestra su tabla de multiplicar con un for.


# SOLUCION
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# Ejercicio 3: Adivina el número

# El programa elige un número secreto (ejemplo: 7) y el usuario debe adivinarlo.
# Usa un while para seguir intentando hasta que acierte.



# SOLUCION
secreto = 7
adivina = None
while adivina != secreto:
    adivina = int(input("Adivina el número secreto (entre 1 y 10): "))
    if adivina < secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif adivina > secreto:
        print("Demasiado alto. Intenta de nuevo.")
print("¡Felicidades! Adivinaste el número.")
print()

# Ejercicio 4: Calculadora básica

# Pide dos números y una operación (+, -, *, /).
# Usa condicionales para decidir la operación.


# SOLUCION
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")
if operacion == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operacion == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operacion == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operacion == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: División por cero.")
else:
    print("Operación no válida.")
print()

# Ejercicio 5: Contador de vocales

# Pide una palabra y cuenta cuántas vocales tiene con un for.


# SOLUCION
palabra = input("Ingrese una palabra: ")
vocales = 'aeiouAEIOU'
contador = 0
for letra in palabra:
    if letra in vocales:
        contador += 1
print(f"La palabra '{palabra}' tiene {contador} vocales.")
print()