#Herança em Python

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print("O animal faz um som genérico.")

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def fazer_som(self):
        print("O cachorro faz o som 'Au au!'")



cao = Cachorro('ted', 3, 'chiaua')
print(cao)
cao.fazer_som()