# Ejercicio 1: Números pares e impares
# Pide un número al usuario y muestra si es par o impar.
# Luego, imprime todos los números pares hasta ese número.

# SOLUCION
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")

print("Números pares hasta", numero, ":")
for i in range(2, numero + 1, 2):
    print(i)


# ----------------------------------------------------------------------
# Ejercicio 2: Tabla de multiplicar
# Pide un número y muestra su tabla de multiplicar con un for.

# SOLUCION
num = int(input("\nIngresa un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# ----------------------------------------------------------------------
# Ejercicio 3: Adivina el número
# El programa elige un número secreto (ejemplo: 7) y el usuario debe adivinarlo.
# Usa un while para seguir intentando hasta que acierte.

# SOLUCION
secreto = 7
intento = None

print("\n¡Adivina el número secreto entre 1 y 10!")
while intento != secreto:
    intento = int(input("Tu intento: "))
    if intento < secreto:
        print("El número secreto es mayor.")
    elif intento > secreto:
        print("El número secreto es menor.")
print("¡Correcto! El número secreto era", secreto)


# ----------------------------------------------------------------------
# Ejercicio 4: Calculadora básica
# Pide dos números y una operación (+, -, *, /).
# Usa condicionales para decidir la operación.

# SOLUCION
print("\nCalculadora básica")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
operacion = input("Que deseas hacer ? (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", a + b)
elif operacion == "-":
    print("Resultado:", a - b)
elif operacion == "*":
    print("Resultado:", a * b)
elif operacion == "/":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida")


# ----------------------------------------------------------------------
# Ejercicio 5: Contador de vocales
# Pide una palabra y cuenta cuántas vocales tiene con un for.

# SOLUCION
palabra = input("\nIngresa una palabra: ").lower()
vocales = "aeiou"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"La palabra '{palabra}' tiene {contador} vocal(es).")

# - - - - - - --  -- - - - - - - - - - - - -- -  -- - - - - - - - - -- - -  -- - - -
# - - - - --  IMPORTANTE - - - - - -- 

# La solución debe hacerla en su rama respectiva, plazo maximo viernes 19/09/2025 a las 12 PM (Noche)
