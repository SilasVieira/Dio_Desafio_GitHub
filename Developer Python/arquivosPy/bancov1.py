'''Versão 1.0 banco ._Dio '''
# Tela de boas vindas ao usuario, e perguntar oque deseja fazer, Depositar valor, Sacar valor, Extrato.
menu = '''
[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair
=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("informe o valor do deposito: "))
    
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print("Operação falhou o valor informado é invalido. *")

    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Sem saldo suficiente.")
        elif excedeu_limite:
            print("Saque excede limite.")
        elif excedeu_saques:
            print("Saques excedidos.")
        elif valor > 0:
            saldo -= valor
            extrato += f'saque: R${valor:.2f}\n'
            numero_saques += 1

        else:
            print("Falha na operação, valor informado invalido.")

    elif opcao == "e":
        print("\n=========== EXTRATO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("======================")
    
    elif opcao == "q":
        break

    else:
        print("Opção invalida, por favor selecione corretamenta as opções.")