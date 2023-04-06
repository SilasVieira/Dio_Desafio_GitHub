# Sistema de Cadastro de produtos
with open(file='texto.txt', mode='a', encoding='utf-8') as arquivo: # Criamos um arquivo vazio texto.txt
    produto = [] # Criamos uma lista vazia para receber os itens da proxima variavel 
    cadastro_produto = input('Digite o nome do produto:') # Cadastramos o produto nessa variavel
    produto.append(cadastro_produto) # Adicionamos o produto da variavel cadastro_produto na lista produto
    arquivo.write(str(produto) + '\n') # Escrevemos no arquivo o valor da variavel produto e quebramos uma linha.

    

    

    