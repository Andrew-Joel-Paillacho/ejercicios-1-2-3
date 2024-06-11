''' Realice un programa, para calcular la suma de los N primeros
números pares.
Es decir, si insertamos un 8, nos haga la suma de 2+4+6+8.
Recuerda utilizar la sentencia de repetición. '''

valor = int(input("\nIngrese el número para la suma maxima: "))
suma=0

for i in range(1,valor+1):
    if i%2 == 0:
        suma+=i
        
print(f"\nLa suma de numeros pares hasta el {valor}: {suma}")
print()
