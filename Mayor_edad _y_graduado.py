# Paso 1: Pedir los datos al usuario
edad = int(input("Ingrese su edad: "))
graduado = input("¿Ya se graduó del colegio? (si/no): ")

# Paso 2: Determinar si es mayor de edad
es_mayor = edad >= 18
if es_mayor:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

# Paso 3: Determinar si ya se graduó
es_graduado = graduado == "si"
if es_graduado:
    print("Ya se graduó del colegio.")
else:
    print("No se ha graduado del colegio.")

# Resumen opcional
print("La persona tiene " + str(edad) + " años y " + "está graduado")