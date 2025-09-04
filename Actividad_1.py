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
nombre = "Christian"
apellido = "Bolaños"
print("Nombre:", nombre)
print("Apellido:", apellido)

# Variables tipo entero
num1 = 10
num2 = 5
print("Número 1:", num1)
print("Número 2:", num2)

# Concatenación de strings
concatenacion = nombre + " " + apellido
print("Concatenación:", concatenacion)

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

# Definir arreglo mixto (números y letras)
mi_arreglo = [10, 20, "A", "B", 5]

# Imprimir arreglo completo
print("Arreglo completo:", mi_arreglo)

# Primer elemento
print("Primer elemento:", mi_arreglo[0])

# Último elemento
print("Último elemento:", mi_arreglo[-1])

# Suma, resta, multiplicación entre primer y último (solo si son números)
print("Suma primer y último:", mi_arreglo[0] + mi_arreglo[-1])
print("Resta primer y último:", mi_arreglo[0] - mi_arreglo[-1])
print("Multiplicación primer y último:", mi_arreglo[0] * mi_arreglo[-1])




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
"""
Parte 3

R/ CI/CD significa Integración Continua (Continuous Integration) y Despliegue/Entrega Continua (Continuous Deployment/Delivery). 
Es una práctica que automatiza la integración de código, pruebas y despliegues para garantizar calidad y rapidez en el desarrollo.

R/ Herramientas para desplegar aplicaciones:
- Docker, Kubernetes, Heroku, AWS, Azure, Google Cloud.

R/ Herramientas para automatizar despliegues:
- Jenkins, GitHub Actions, GitLab CI/CD, CircleCI, Travis CI.

R/ Herramientas en Python para automatizar pruebas:
- pytest, unittest, nose2, tox.
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

ENLACE A MI REPOSITORIO: 

"""
# ENLACE A MI REPOSITORIO: 
# https://github.com/ChristianBolaños/ci-cd-practicas
