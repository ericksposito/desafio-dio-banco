menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = input("Qual o valor deseja depositar: ")
        extrato += "Deposito de R$"+deposito+"\n\n"
        saldo += float(deposito)
        print(extrato)
        print(saldo)
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Número de saques excedidos")
        else:
            print("Saque")
            saque = input("Qual o valor deseja sacar: ")
            if float(saque) > saldo:
                print("Saldo insuficiente pra o valor informado")
            else:
                extrato += "Saque de R$"+saque+"\n\n"
                saldo -= float(saque)
                print(extrato)
                print(saldo)
                numero_saques += 1

    elif opcao == "e":
        print("Extrato")
        imprime_saldo = float(saldo)
        print(f"""Este é o seu extrado: \n\n{extrato} \nSeu saldo atual é de R${imprime_saldo:2}""")
    
    elif opcao == "q":
        print("Sair")
        print("Obrigado por utilizar nosso sistema")
        break

    else:
        print("Operação inválida, por favor selecione uma das opções")