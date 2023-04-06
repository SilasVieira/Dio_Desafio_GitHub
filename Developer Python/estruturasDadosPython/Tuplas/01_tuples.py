fruta = ("Laranja", "Pera", "Uva",)
letras = tuple("Python")
numeros = tuple([1,2,3,4,]) # listas será convertido para tuples e não podem mais ser mutaveis
pais = ("Brasil",) 

#sempre bom colocar uma virgula no final para que o 
#interpretador python saiba que é uma tuple.

print(fruta[0])
print(fruta[1])
print(fruta[-1])

fruta_2 = (("Laranja", "Pera", "Uva"),("Ovo", "Sal", "Oléo",),("Python","Ruby"),)
print(fruta_2)

tupla = ("P","h","y","t","o","n",)

print(f'{tupla[2:]}')
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::1])
print(tupla[::-1])

for frutas in fruta:
    print(frutas)