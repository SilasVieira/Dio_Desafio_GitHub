# Vamos tentar criar um dicionario em python
with open(file='iventario.txt', mode='a', encoding='utf-8') as arquivo: # Criamos um arquivo vazio texto.txt

    itens = {} # criamos um dicionario vazio que vai receber os valores das variaveis seguintes

    cadastro_item = input('Digite o nome do item: ') # usuario digita o nome do item.
    cadastro_valor = input('Digite o valor do item: ') # usuario digita o nome do valor 'preço'.

    itens[cadastro_item] = f'R$ {cadastro_valor}' # aqui adicionamos os valores no dicionario vazio
    arquivo.write(str(itens) + '\n')

print(itens)

