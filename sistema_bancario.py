menu = """
    ======MENU======

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

    => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    try:
        escolha = int(input(menu))

        match escolha:
            case 1:
                deposito = float(input("Digite o valor a ser adicionado: "))
                if deposito > 0:
                    saldo += deposito
                    extrato += (f"Depósito: R$ {deposito:.2f}\n")
                    print(f"Valor depositado com sucesso!\nSeu saldo atual é: R${saldo:.2f}")
            
                else:
                    print("Valor Inválido!")

            case 2:
                sacar = float(input("Digite o valor a ser sacado: "))

                if (sacar <= saldo) and (sacar <= limite) and (LIMITE_SAQUES > numero_saques) and (sacar > 0):
                    print (f"O valor de: R${sacar} foi sacado com sucesso!")
                    saldo -= sacar
                    extrato += (f"Saque: R$ {sacar:.2f}\n")
                    numero_saques += 1

                elif LIMITE_SAQUES <= numero_saques:
                        print("Limite de saques por dia atingido! Tente novamente amanhã")

                elif (sacar > limite):
                    print (f"O saque de R${sacar} é maior que o limite de R${limite}")
                
                elif (sacar > saldo):
                    print (f"Não foi possível sacar o valor desejado, pois ele é maior que o saldo da conta\nSaldo atual: R${saldo}")

                else:
                    print("Valor inválido!")
            
            case 3:
                print('''   ======Extrato======''')

                if not extrato:
                    print("\nNão houve movimentações em sua conta")

                else:
                    print(f"{extrato}\nSaldo atual: R${saldo}")

            case 4:
                break

            case _:
                print ("Opção Inválida! Selecione novamente a opção desejada")       

    except ValueError:
        print("Opção Inválida! Digite um número para selecionar a opção desejada.")