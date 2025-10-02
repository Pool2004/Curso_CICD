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


# Variables de tipo String
nombre = "Juan" 
apellido = "Pérez"
print("Nombre:", nombre)
print("Apellido:", apellido)
# Concatenación de variables String
nombre_completo = nombre + " " + apellido
print("Nombre Completo:", nombre_completo)
# Variables de tipo entero
num1 = 10
num2 = 3
print("Número 1:", num1)
print("Número 2:", num2)
# Operaciones con variables enteras
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
modulo = num1 % num2
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División Entera:", division_entera)
print("Módulo:", modulo)


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
# Definición del arreglo con números y letras
arreglo = [10, 'a', 20, 'b', 30]
print("Arreglo completo:", arreglo)
# Imprimir el primer elemento del arreglo por posición
print("Primer elemento:", arreglo[0])
# Imprimir el último elemento del arreglo por posición
print("Último elemento:", arreglo[-1])
# Imprimir la suma entre el primer valor del elemento y el último
suma = arreglo[0] + arreglo[-1]
print("Suma del primer y último elemento:", suma)
# Imprimir la resta entre el primer valor del elemento y el último
resta = arreglo[0] - arreglo[-1]
print("Resta del primer y último elemento:", resta)
# Imprimir la multiplicación entre el primer valor del elemento y el último
multiplicacion = arreglo[0] * arreglo[-1]
print("Multiplicación del primer y último elemento:", multiplicacion)


"""
Parte 3

Responda. ¿Qué es CI/CD?

R//  CI/CD significa Integración Continua (Continuous Integration) y Despliegue/Entrega Continua (Continuous Deployment/Delivery).
Es un conjunto de prácticas y herramientas que permiten integrar, probar y desplegar código automáticamente, asegurando calidad y rapidez en el desarrollo de software.

Responda. ¿Qué herramientas hay para desplegar aplicaciones?

R// Algunas herramientas populares para desplegar aplicaciones incluyen:
- Jenkins
- GitLab CI/CD
- Travis CI
- CircleCI
- Docker
- Kubernetes

Responda. ¿Qué herramientas hay para automatizar despliegues?

R//  Algunas herramientas para automatizar despliegues son:
- Ansible
- Terraform
- Chef
- Puppet


Responda. ¿Qué herramientas en python para automatizar pruebas?
R//  Algunas herramientas en Python para automatizar pruebas son:
- pytest
- unittest
- nose2
- Robot Framework
- Behave

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

