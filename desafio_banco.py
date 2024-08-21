import datetime
import textwrap
data = datetime.datetime.now().strftime("%d/%m/%Y  %H:%M:%S")


def main():
    LIMITE_SAQUE= 3
    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    extrato =""
    numero_saques= 0
    usuarios =[]
    contas = []
    

    while True:
        opcao = menu()
        
        if opcao == 'd':
            valor = float(input('Informe o valor do deposito: '))
            
            saldo,extrato =  depositar(saldo,valor,extrato)
            
        elif opcao == 's':
             valor = float(input('Informe o valor do saque: '))
             saldo,extrato = sacar(
                 saldo=saldo,
                 valor=valor,
                 extrato=extrato,
                 limite=limite,
                 numero_saques = numero_saques,
                 limite_saques= LIMITE_SAQUE,
             )
             
        elif opcao == 'e':
            exibir_extrato(saldo,extrato=extrato)
        
        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                conta.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'q':
            break

def menu():
    menu = """
    [d]\t  Depositar
    [s]\t  Sacar
    [e]\t  Extrato
    [nc]\t Nova Conta
    [lc]\t Listar Contas
    [nl]\t Novo Cliente
    [q]\t Sair
    =>
    """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f" Depósito: \t\tR$: {valor:.2f} \t{data} \n"
        print("\n 💸 Depósito realidaso com sucesso ✅")
    else:
        print("\n ❌ Operação falhou! O valor informado é inválido ❌")
        
    return saldo,extrato
        
def sacar(*,saldo,valor,extrato,limite, numero_saques, limite_saques):
    exedeu_saldo = valor > saldo
    exedeu_limte = valor > limite
    exedeu_saques = numero_saques >= limite_saques
    
    if exedeu_saldo:
        print("\n ❌ Operação falhou! Saldo insuficiente para saque ❌")
    elif exedeu_limte:
        print("\n ❌ Operação falhou! O valor do saque excedeu o limite ❌")
    elif exedeu_saques:
        print("\n ❌ Operação falhou! Número de saques excedido ❌")
        
    elif valor > 0:
        saldo -=  valor
        extrato += f' Saque \t\t R$: {valor:.2f} \t{data} '
        numero_saques += 1
        print("\n 💸 Saque realidaso com sucesso ✅")
    else:
         print("\n ❌ Operação falhou! O valor informado é invalido ❌")
         
    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
     print("\n ======================EXTRATO======================")
     print('Não foram realizadas movimentações.' if not extrato else  extrato)
     print(f'\n Saldo: \t\tR$ {saldo:.2f}')
     print("\n ===================================================")
     
def criar_usuario(usuarios):
    cpf = input('Informe o seu CPF (somente numeros): ')
    usuario = filtar_usuario(cpf,usuarios)
    if usuario:
        print("\n ❌ Operação falhou! Usuario já cadastrado ❌")
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Inform a data de nascimento (dd-mm-aaaa): ')
    endereco= input('Informe o endereço (Logradouro, nº - bairro - cidade/sigla estado):')
    
    usuarios.append({'nome': nome, 'data-nascimento': data_nascimento, 'cpf':cpf, 'endereço': endereco})
    print('✅ Usuario criado com sucesso ✅')
    
def filtar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
   cpf = input('Informe o seu CPF (somente numeros): ')
   usuario = filtar_usuario(cpf,usuarios)
   if usuario:
       print('✅ Conta criado com sucesso ✅')
       return {"agencia": agencia, "numero_conta":numero_conta, "usuario": usuario}
   
   print('❌ Operação falhou! Usuario não encontrato ❌')
   
   
def listar_contas():
   pass
        
        

main()