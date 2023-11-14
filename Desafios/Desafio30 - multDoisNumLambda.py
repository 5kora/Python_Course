inputUser1 = int(input("Digite o primeiro numero da multiplicação: "))
inputUser2 = int(input("Digite o segundo numero da multiplicação: "))

multNumbers = lambda x,y : x * y

print(f'O resultado de {inputUser1} * {inputUser2} = {multNumbers(inputUser1, inputUser2)}')