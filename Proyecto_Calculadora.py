# Se ingresan los valores a las variables agregando las restricciones de los tipos de las variables
Nombre= input('Ingresa tu nombre:')
ApellidoPaterno= input('Ingresa tu apellido paterno:')
ApellidoMaterno= input('Ingresa tu apellido materno:')

# Función para solicitar un número entero
def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor digita tu edad numérica.")

# Función para solicitar un número flotante
def solicitar_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor digita tu peso numérico.")

Edad = solicitar_entero('Ingresa tu edad:')
Peso = solicitar_flotante('Ingresa tu peso:')
Estatura = solicitar_flotante('Ingresa tu estatura:')

# Se calcula el índice de masa corporal mediante la formula: peso/estatura2
MasaCorporal= Peso / (Estatura ** 2)

print("Tu nombre es {} {} {} y tu índice de masa corporal es {}".format(Nombre, ApellidoPaterno, ApellidoMaterno, MasaCorporal))
