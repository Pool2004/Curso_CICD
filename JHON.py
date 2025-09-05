# hola

# Declarar 2 variables de tipo String y mostrarlas
texto1 = "Hola"
texto2 = "Mundo"
print(texto1)
print(texto2)

# Declarar 2 variables de tipo entero y mostrarlas
num1 = 12
num2 = 4
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


#    Parte dos


# Definir un arreglo de números y letras con longitud mínima de 5 elementos
arreglo = [5, 'X', 8, 'Y', 3]

# Imprimir el arreglo en consola
print(arreglo)

# Imprimir el primer elemento por posición
print("Primer elemento:", arreglo[0])

# Imprimir el último elemento por posición
print("Último elemento:", arreglo[4])

# Imprimir la suma entre el primer y último elemento (solo si ambos son números)
if isinstance(arreglo[0], int) and isinstance(arreglo[-1], int):
    print("Suma:", arreglo[0] + arreglo[-1])
    print("Resta:", arreglo[0] - arreglo[-1])
    print("Multiplicación:", arreglo[0] * arreglo[-1])
else:
    print("No se puede operar suma/resta/multiplicación entre tipos diferentes.")


    # parte 3 

"""
¿Qué es CI/CD?
R/ CI/CD significa Integración Continua y Despliegue/Entrega Continua .
Es una práctica de desarrollo de software que automatiza la integración de cambios de código,
pruebas y despliegue en entornos de producción, reduciendo errores humanos y acelerando la entrega de nuevas versiones.

¿Qué herramientas hay para desplegar aplicaciones?
R/ Algunas herramientas comunes para desplegar aplicaciones son:
Kubernetes
Heroku
AWS Elastic Beanstalk
Google Cloud Run
Microsoft Azure App Service
Netlify 
¿Qué herramientas hay para automatizar despliegues?
R/ Herramientas populares de automatización de despliegues:
Jenkins
GitLab CI/CD
GitHub Actions
CircleCI
Travis CI
Ansible
Terraform

¿Qué herramientas en Python para automatizar pruebas?
R/ Librerías y frameworks más usados en Python para pruebas:
unittest 
pytest 
nose2
Behave (para pruebas BDD)
Robot Framework
Selenium (para pruebas de UI)
"""


# parte 4 

# mi repositorio es https://github.com/Jhonj877/myJhon.git