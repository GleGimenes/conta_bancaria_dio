saldo = 1500
saques_realizados = 0
extrato = []

opcao = -1

while opcao != 0:
    opcao = int(input('[1] Saque \n[2] Deposito \n[3] Extrato \n[0] Sair \nEscolha uma opção: '))
    if opcao == 1:
        print('Saque')
        if saques_realizados < 3: 
            valor = int(input('Digite o valor a ser sacado: '))
            limite_por_saque = 500
            if valor <= 0:
                print('Valor inválido')
            elif valor > saldo:
                print('Saldo insuficiente')
            elif valor > limite_por_saque:
                print('Saque não autorizado. Valor limite permitido por saque é 500.')
            else:
                saldo -= valor
                saques_realizados += 1  
                print(f'Saldo atual: R${saldo:.2f}')
                print(f'Saques restantes hoje: {3 - saques_realizados}')
                extrato.append(f'Saque: R${valor:.2f}')
        else:
            print('Limite de 3 saques diários atingido.')
    elif opcao == 2:
        print('Deposito')
        valor = int(input('Digite o valor a ser depositado: '))
        if valor > 0: 
            saldo += valor
            print(f'Deposito realizado com sucesso!')
            extrato.append(f'Depósito: R${valor:.2f}')
        else:
            print('Valor inválido') 
    elif opcao == 3:
        print('Extrato')
        print('Extrato bancário')
        print('-----------------')
        for operacao in extrato:
            print(operacao)
        print(f'Saldo atual: R${saldo:.2f}')
        print('-----------------')
    elif opcao == 0:
        print('Obrigado por utilizar nossos serviços!')
    else:
        print('Opção inválida')
