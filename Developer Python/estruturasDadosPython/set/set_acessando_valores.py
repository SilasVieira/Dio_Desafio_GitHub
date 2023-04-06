numeros = {1,2,3,4,5}
numeros = list(numeros)
print(numeros[0])

for indice, numero in enumerate(numeros):
    print(f'{indice}: {numero}')