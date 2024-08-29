
print("======= Bem vindo ao Sistema Bancário básico de Macauli =======")

menu = '''Digite a tecla da operação que deseja realizar!!!
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valorDeposito = float(input("Qual valor você gostaria de depositar? "))
        
        if valorDeposito > 0:
            saldo += valorDeposito
            extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
            print(f"Depósito de R$ {valorDeposito:.2f} realizado com sucesso!")
        else:
            print("Operação inválida! O valor do depósito deve ser positivo.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Você já atingiu o limite de saques diários.")
        else:
            valorSaque = float(input(f"Quanto você deseja sacar? Seu saldo atual é de R$ {saldo:.2f}\n"))
            
            if valorSaque > saldo:
                print("Saldo insuficiente!")
            elif valorSaque > limite:
                print(f"O valor do saque excede o limite de R$ {limite:.2f}")
            elif valorSaque > 0:
                saldo -= valorSaque
                extrato += f"Saque: R$ {valorSaque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valorSaque:.2f} realizado com sucesso!Seu saldo atual agora é R$ {saldo}")
            else:
                print("Operação inválida! O valor do saque deve ser positivo.")

    elif opcao == "e":
        print("\n========== Extrato ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")

