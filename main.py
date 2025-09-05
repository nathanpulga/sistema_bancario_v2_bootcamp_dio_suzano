def menu():
    return """
    ****** Sistema Bancário V2 *******

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuario
    [5] Nova Conta
    [6] Listar Contas
    [7] Listar Usuarios
    [0] Sair

    *******************************
    """

def depositar(saldo, valor, extrato,/):
    # positional only argument
    if valor >0:
        print (f'\nDepósito de R${valor} realizado com sucesso \n')
        saldo += valor
        extrato += f'Depósito R${valor} \n'
    else:
        print('Erro ao gerar operação, por favor insira um valor válido')

    return saldo, extrato
    
def sacar(*,saldo, valor, extrato, numero_saques, limite_saques,limite):
    # keyword only argument
    if (numero_saques <= limite_saques) and (valor <= limite) and (valor <= saldo):
        print (f'\nSaque de R${valor} realizado com sucesso \n')
        saldo -= valor
        extrato += f'Saque R${valor} \n'
        numero_saques +=1
    elif valor > saldo:
        print ('Saldo insuficiente')
    elif valor > limite:
        print (f'Limite de saque por operação de R${limite}. Por favor insira um valor menor')
    elif numero_saques >= limite_saques:
        print ('Quantidades de saques diárias atingidas. Por favor retorne amanhã')
    else:
        print('Erro ao processar a operação, tente mais tarde.')

    return saldo, extrato, numero_saques
    

def exibir_extrato(saldo, /,*, extrato):
    #positional only argument
    print("\n*********** EXTRATO ***********")
    print(f" {extrato}")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("*******************************")
    
def verificar_usuario(usuarios,cpf):
    return bool([usuario for usuario in usuarios if usuario['cpf'] == cpf])

def criar_usuario(usuario):
    # cliente do banco
    cpf = str(input("Informe o cpf do usuario: "))
    if verificar_usuario(usuario,cpf):
        print("Usuario já existe")
        return
    else:
        nome = str(input("Informe o nome do usuario: "))
        data_nascimento = str(input("Informe a data de nascimento do usuario: "))
        endereco = str(input("Informe o endereço do usuario: "))
        user = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco,
        }
        print(f'Usuario {nome} criado com sucesso')
        usuario.append(user)
        
def criar_conta(usuario,conta,agencia):
    # vincular conta ao usuario
    contas = {
        'agencia': agencia,
        'conta': conta,
        'usuario': usuario,
        }
    print(f'Conta {conta} criada com sucesso')
    return contas

def listar_usuarios(usuario):
    for user in usuario:
        linha = f"""\
        Nome:\t{user['nome']}
        CPF:\t{user['cpf']}
        """
        print(linha)

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Usuario:\t{conta['usuario'][0]['nome']}
        CPF:\t{conta['usuario'][0]['cpf']}
        Agencia:\t{conta['agencia']}
        C/C:\t{conta['conta']}
        """
        print(linha)

def sistema_bancario():
    usuarios = []
    contas = []
    agencia = "0001"
    conta = 0
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques  = 1
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu())
        if opcao == '1':
            valor = float(input('Insira o valor para deposito R$ '))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == '2':
            valor = float(input('Insira o valor para saque R$ '))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, numero_saques=numero_saques, limite_saques= LIMITE_SAQUES,limite = limite)

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            criar_usuario(usuarios)

        elif opcao == '5':
            #criar conta
            cpf = str(input("Informe o cpf do usuario: "))
            if verificar_usuario(usuarios,cpf):
                conta += 1
                contas_criadas = criar_conta(usuarios,conta,agencia)
                contas.append(contas_criadas)
            else:
                print("Usuario não encontrado")
                
        elif opcao == '6':
            listar_contas(contas)

        elif opcao == '7':
            listar_usuarios(usuarios)

        elif opcao == '0':
            print ('Sair')
            break
        else:
            print('Opção inválida, tente novamente')

if __name__ == "__main__":
    sistema_bancario()
