# Criando um sistema de Cadastro de peças
import datetime

with open(file='Cadastro_Itens.txt', mode='a', encoding='utf-8') as arquivo: # Criamos um arquivo vazio Cadastro_Itens.txt
    itens = {} # Criamos um dicionario vazio
    

    while True: # Criamos um loop While enquanto for verdadeiro


        nome_item = input('Digite o nome do item (ou digite "sair" para sair): ') # Pedimos ao usuario digitar
        if nome_item == 'sair': # Criamos uma condição para que o usuario saia do processo de loop

            break

        preco_item = input('Digite o preço do item: ') # Criamos a condição para digitar o nome do item e preço

        preco_item = float(preco_item)

        now = datetime.datetime.now() # Obtém a data e hora atuais

        timestamp = now.strftime("%d/%m/%Y %H:%M:%S") # Formata a data e hora em uma string legível

        itens[f'Produto: {nome_item}'] = f'R$: {preco_item:.2f}, // Data-({timestamp}hs)' # Aqui fiz com que ao digitar apenas numero inteiro retorna numero flutuante ex: 10 vai retornar 10.00   
    

    for item, preco in itens.items(): # Fazemos o loop for percorrer item e preço no dicionario de itens

        arquivo.write(f'{item}: {preco}\n') # Essa linha escreve uma string no arquivo, com o nome do item e seu respectivo preço, seguido por uma quebra de linha ("\n"), que é utilizada para separar as linhas no arquivo.
    
print(f'{itens} \n')
