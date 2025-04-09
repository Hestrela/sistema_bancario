from datetime import date

def menu():
    menu = """
        ======MENU======

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Novo Usuário
        [5] Criar Conta
        [6] Listar Contas
        [7] Sair

        => """

    return int(input(menu))

def depositar (saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += (f"Depósito: R$ {deposito:.2f}\n")
        print(f"Valor depositado com sucesso!\nSeu saldo atual é: R${saldo:.2f}")
                
    else:
        print("Valor Inválido!")

    return saldo, extrato

def sacar (*, saldo, saque, extrato, limite, numero_saques, limite_saques):

    if limite_saques < numero_saques:
        print("Limite de saques por dia atingido! Tente novamente amanhã")

    elif (saque > limite):
        print (f"O saque de R${sacar} é maior que o limite de R${limite}")
                
    elif (saque > saldo):
        print (f"Não foi possível sacar o valor desejado, pois ele é maior que o saldo da conta\nSaldo atual: R${saldo}")

    elif (saque < 0):
        print("Valor inválido!")
    
    else:
        print (f"O valor de: R${saque} foi sacado com sucesso!")
        saldo -= saque
        extrato += (f"Saque: R$ {saque:.2f}\n")
        numero_saques += 1

    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n========= Extrato =========")

    if not extrato:
        print("\nNão houve movimentações em sua conta")

    else:
        print(f"{extrato}\nSaldo atual: R${saldo}")

def validar_cpf(cpf, usuarios):
    usuarios_validados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_validados[0] if usuarios_validados else None

def criar_usuario(usuarios):
    nome = input("Digite seu Nome: ")
    cpf = input("Digite seu CPF (somente números): ")
    usuario = validar_cpf(cpf, usuarios)

    data_nascimento = input("Digite sua data de nascimento (dd/mm/AAAA):")
    endereco = input("Digite seu endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({"nome" : nome, "cpf" : cpf, "Data de Nascimento" : data_nascimento, "Endereço" : endereco})

    print("Usúario criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF (somente números): ")
    usuario = validar_cpf(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print(linha)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        escolha = menu()

        try:
            match escolha:
                case 1:
                    deposito = float(input("Digite o valor a ser adicionado: "))
                    
                    saldo, extrato = depositar(saldo, deposito, extrato)

                case 2:
                    saque = float(input("Digite o valor a ser sacado: "))

                    saldo, extrato = sacar(saldo=saldo, saque=saque, extrato=extrato, 
                    limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
                
                case 3:
                    mostrar_extrato(saldo, extrato=extrato)

                case 4:
                    criar_usuario(usuarios)

                case 5:
                    numero_conta = len(contas) + 1
                    conta = criar_conta(AGENCIA, numero_conta, usuarios)

                    if conta:
                        contas.append(conta)
                        
                
                case 6:
                    listar_contas(contas)

                case 7:
                    break

                case _:
                    print("Opção Inválida!")

        except ValueError:
            print("Opção Inválida! Digite um número para selecionar a opção desejada.")


main()