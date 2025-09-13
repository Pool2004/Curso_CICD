# Grupo de Cristian - Variables iniciales y input de cantidad de estudiantes


# grupo de christian - mostrar  Variables iniciales y input de cantidad de estudiantes

cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
nombres = []
notas = []


# Grupo de Jhon - Ciclo while preguntando nombre y nota y agregando a los arreglos
i = 0  
while i < cantidad_estudiantes:
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
    nombres.append(nombre)
    notas.append(nota)
    i += 1




# Grupo de Juan - Promedio general de notas y condicionales

promedio = sum(notas) / len(notas)

if (promedio >= 3.0):
    print("El curso esta aprobado")
else:
    print("El curso esta reprobado")





# Grupo de Jean - For con nombre y nota, uniendo con zip y mostrando por estudiante nombre, nota y estado con condicional terciario

for nombre, nota in zip(nombres, notas):
    print(f"Estudiante: {nombre}, Nota: {nota}, estado: {'Aprobado' if nota >= 3.0 else 'Reprobado'}")  


    
