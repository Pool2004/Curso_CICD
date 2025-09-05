# Actividad - 1

# Curso CI/CD (Despliegue y automatización de aplicaciones)

# Tema: Python Básico

# Docente: Ing. Jean Paul Ordoñez Ibarguen

# Fecha Entrega Máxima: 05/09/25

# Forma entrega: Rama personal

# Formato Actividad_1_Nombre_Apellido.py

# ----------------------------------------------------------------



"""
Parte 1

- Declare 2 variables de tipo String (Cadena o texto) y luego imprima cada una en consola

- Declare 2 variables de tipo entero (int) y luego imprima cada una en consola

- Con las variables de tipo String, realiza la concatenación de ambas, imprimiendo el resultado en consola.

- Con las variables de tipo entero, realiza la suma, resta, multiplicación, división, división entera, módulo entre ambas. Recuerde imprimir los resultados en consola.

"""

# PONER SOLUCIÓN PARTE 1

# Variables tipo String
print(" ")

texto1 = "Hola"
texto2 = "Mundo"
print(texto1)
print(texto2)

print(" ")

# Variables tipo entero
num1 = 10
num2 = 3
print(num1)
print(num2)

print(" ")

# Concatenación de Strings
print(texto1 + " " + texto2)

print(" ")

# Operaciones con enteros
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)  # División normal (float)
print("División entera:", num1 // num2)  # Cociente entero
print("Módulo:", num1 % num2)  # Resto

print(" ")




"""
Parte 2

- Defina un arreglo de números y letras con longitud mínima de 5 elementos
- Imprima el arreglo en consola.
- Imprimaa el primer elemento del arreglo por posición
- Imprimaa el último elemento del arreglo por posición
- Imprima la suma entre el primer valor del elemento y el último (Recuerde tomarlo por nombreArreglo[Posición])
- Imprima la resta entre el primer valor del elemento y el último (Recuerde tomarlo por nombreArreglo[Posición])
- Imprima la multiplicación entre el primer valor del elemento y el último (Recuerde tomarlo por nombreArreglo[Posición])

"""

# PONER SOLUCIÓN PARTE 2

arreglo = [5, "A", 10, "B", 2]

# Imprimir arreglo completo
print(arreglo)

# Primer elemento (posición 0)
print("Primer elemento:", arreglo[0])

# Último elemento (posición -1)
print("Último elemento:", arreglo[-1])

# Como la suma, resta y multiplicación solo tienen sentido con números,
# tomamos el primer y último elemento que son números (5 y 2 en este caso)

print("Suma:", arreglo[0] + arreglo[-1])
print("Resta:", arreglo[0] - arreglo[-1])
print("Multiplicación:", arreglo[0] * arreglo[-1])


"""
Parte 3

Responda. ¿Qué es CI/CD?

R/
CI/CD significa Integración Continua (Continuous Integration) y Entrega/Despliegue Continuo (Continuous Delivery/Deployment).
Es una práctica de desarrollo de software que busca automatizar la integración de código, pruebas y despliegues
para entregar software de forma más rápida y confiable.

Responda. ¿Qué herramientas hay para desplegar aplicaciones?

R/
Algunas herramientas son: Docker, Kubernetes, Heroku, AWS, Azure, Google Cloud, Netlify, Vercel.

Responda. ¿Qué herramientas hay para automatizar despliegues?

R/
Jenkins, GitHub Actions, GitLab CI/CD, CircleCI, Travis CI, ArgoCD.

Responda. ¿Qué herramientas en python para automatizar pruebas?
R/
Algunas son: unittest, pytest, nose2, doctest, behave (para pruebas BDD).
"""







"""
Parte 4 

- Cree un repositorio personal donde va a gestionar sus despliegues y proyectos
- Cree una carpeta en su maquina donde almacenara su repositorio creado
- Clone el repositorio dentro de la carpeta
- Modifique su archivo README poniendo el enlace de su repositorio


(Tenga en cuenta):

• El repositorio debe ser público
• El repositorio debe tener su respectivo README
• Debe adjuntar el enlace en este documento


"""
# ENLACE A MI REPOSITORIO: https://github.com/juancrakk45/juan_Cifuentes.git
