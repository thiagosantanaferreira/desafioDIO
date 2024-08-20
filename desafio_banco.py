menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>
"""
saldo =0
limite = 500
extrato =""
numeros_saque= 0
LIMITE_SAQUE= 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input('Informe o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Deposito de: R$ {valor:.2f}\n'
        else:
            print('Operação falhou ! O valor informado é invalido')
            
    elif opcao == 's':
        valor = float(input('Informe o vlaor do saque: '))
        exedeu_saldo = valor > saldo
        exedeu_limite = valor > limite
        exedeu_saques = numeros_saque >= LIMITE_SAQUE
        
        if exedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif exedeu_limite:
            print('Operação falhou! Limite de saque não autorizado.')
        elif exedeu_saques:
            print('Operação falhou! Número máximo de saques excedido')
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}"
            numeros_saque += 1
        else:
            print('Operação Falhou! O valor informado é inválido')
            
    elif opcao == 'e':
        print("\n ============EXTRATO============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
        print("\n ===============================")
      
    elif opcao =='q':
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')