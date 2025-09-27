# Ejercicio 1: Números pares e impares
# Pide un número al usuario y muestra si es par o impar.
# Luego, imprime todos los números pares hasta ese número.

# SOLUCION
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
print("Números pares hasta", num, ":")
for i in range(2, num+1, 2):
    print(i)

# -  - - - - -- - - - - - - - - - - - - - - - -- - - - - - - - - - - - -- - - - - -
# Ejercicio 2: Tabla de multiplicar

# Pide un número y muestra su tabla de multiplicar con un for.

# SOLUCION
tabla = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{tabla} x {i} = {tabla * i}")

# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -

# Ejercicio 3: Adivina el número

# El programa elige un número secreto (ejemplo: 7) y el usuario debe adivinarlo.
# Usa un while para seguir intentando hasta que acierte.

# SOLUCION
secreto = 6
adivina = int(input("Adivina el número secreto entre 1 y 10: "))
while adivina != secreto:
    print("Incorrecto, intenta de nuevo.")
    adivina = int(input("Adivina el número secreto entre 1 y 10: "))
print("¡Correcto!")

# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -

# Ejercicio 4: Calculadora básica

# Pide dos números y una operación (+, -, *, /).
# Usa condicionales para decidir la operación.

# SOLUCION
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
op = input("Ingrese la operación (+, -, *, /): ")
if op == "+":
    print("Resultado:", a + b)
elif op == "-":
    print("Resultado:", a - b)
elif op == "*":
    print("Resultado:", a * b)
elif op == "/":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("No se puede dividir por cero.")
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
print("Cantidad de vocales:", contador)

# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -
# - - - - --  IMPORTANTE - - - - - -- 

# La solución debe hacerla en su rama respectiva, plazo maximo viernes 19/09/2025 a las 12 PM (Noche)
