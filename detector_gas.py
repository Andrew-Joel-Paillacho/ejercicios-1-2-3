
'''Automotores “Chevrolet” desea colocar sensores para detectar fugas de
gas y que mande alertas respectivas. En ese sentido, se desea programar
un sensor de gas para un Arduino, la tarea consiste en que el sensor
obtenga la información de 3 talleres mecánicos y que contabilice si
existe fuga de gas. En el que, si el número de talleres es mayor a 1 se
debe mandar un correo al usuario alertando de la novedad, caso
contrario no se realizará ninguna acción.'''

def verificar_fugas(talleres):
    fugas_detectadas = sum(talleres)
    if fugas_detectadas > 1:
        print("\nSe ha detectado una fuga de gas en más de un taller. Se enviará un correo de alerta.\n")
    else:
        print("\nNo se requiere ninguna acción.\n")

taller1 = int(input("\n¿Hay fuga de gas en el taller 1? (1 para sí, 0 para no): "))
taller2 = int(input("\n¿Hay fuga de gas en el taller 2? (1 para sí, 0 para no): "))
taller3 = int(input("\n¿Hay fuga de gas en el taller 3? (1 para sí, 0 para no): "))

talleres = [taller1, taller2, taller3]
verificar_fugas(talleres)


