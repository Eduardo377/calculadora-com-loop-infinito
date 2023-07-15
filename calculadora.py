def calculadora():
    while True:
        print("Digite a operação desejada: \n1. Soma \n2. Subtração \n3. Multiplicação \n4. Divisão \n")

        # Solicita a operação desejada ao usuário
        operacao = int(input("Digite o número para a operação correspondente: "))

        if operacao == 0:
            print("Saindo...")
            break

        elif operacao == 1:
            # Realiza a soma de dois valores inseridos pelo usuário
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = num1 + num2
            print(f"Resultado: {resultado}")

        elif operacao == 2:
            # Realiza a subtração de dois valores inseridos pelo usuário
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = num1 - num2
            print(f"Resultado: {resultado}")

        elif operacao == 3:
            # Realiza a multiplicação de dois valores inseridos pelo usuário
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = num1 * num2
            print(f"Resultado: {resultado}")

        elif operacao == 4:
            # Realiza a divisão de dois valores inseridos pelo usuário
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))

            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: Divisão por zero não existe!")

        else:
            # Exibe uma mensagem de erro caso a opção escolhida não seja válida
            print("Essa opção não existe")

        print()

calculadora()
