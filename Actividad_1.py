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

# Parte 1
# Variables tipo String
texto1 = "Hola"
texto2 = "Mundo"
print(texto1)
print(texto2)

# Variables tipo entero
num1 = 10
num2 = 5
print(num1)
print(num2)

# Concatenación de Strings
print(texto1 + " " + texto2)

# Operaciones con enteros
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)
print("División entera:", num1 // num2)
print("Módulo:", num1 % num2)




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

# Parte 2
arreglo = [1, 'a', 3, 'b', 5]
print(arreglo)
print("Primer elemento:", arreglo[0])
print("Último elemento:", arreglo[-1])

# Solo suma, resta y multiplicación si ambos son números
if isinstance(arreglo[0], int) and isinstance(arreglo[-1], int):
    print("Suma:", arreglo[0] + arreglo[-1])
    print("Resta:", arreglo[0] - arreglo[-1])
    print("Multiplicación:", arreglo[0] * arreglo[-1])


"""
Parte 3

Responda. ¿Qué es CI/CD?

R/

Responda. ¿Qué herramientas hay para desplegar aplicaciones?

R/

Responda. ¿Qué herramientas hay para automatizar despliegues?

R/

Responda. ¿Qué herramientas en python para automatizar pruebas?
R/

"""


# PONER SOLUCIÓN PARTE 3

# Parte 3
# ¿Qué es CI/CD?
# R/
# CI/CD significa Integración Continua y Entrega/Despliegue Continuo. Son prácticas para automatizar la integración y entrega de código en proyectos de software.

# ¿Qué herramientas hay para desplegar aplicaciones?
# R/
# Algunas herramientas son: Docker, Kubernetes, AWS, Azure, Heroku.

# ¿Qué herramientas hay para automatizar despliegues?
# R/
# Jenkins, GitHub Actions, GitLab CI, Travis CI.

# ¿Qué herramientas en python para automatizar pruebas?
# R/
# pytest, unittest, nose, behave.

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

ENLACE A MI REPOSITORIO: 
https://github.com/tu_usuario/tu_repositorio
"""
