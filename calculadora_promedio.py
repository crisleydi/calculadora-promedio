print("CALCULADORA DE PROMEDIO")

nombre = input("Ingrese el nombre del estudiante: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print("\nRESULTADO")
print("Estudiante:", nombre)
print("Promedio:", round(promedio, 2))

if promedio >= 51:
    print("Estado: Aprobado")
else:
    print("Estado: Reprobado")