class Bicicleta:

    def __init__(self, cor, modelo, ano, valor) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Trim Trim')
    
    def parar(self):
        print('Bicicleta parando.')
    
    def correr(self):
        print('Vraummmm')


b1 = Bicicleta('Vermelha', 'Caloi', 1999, 200.00)

b1.buzinar()

print(b1.cor, b1.ano)