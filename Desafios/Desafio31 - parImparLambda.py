evenOrOdd = lambda x : f"O numero {x} é par!" if x % 2 == 0 else f"O numero {x} é ímpar!"

inputUser = int(input("Digite um numero para descobrir se é par ou ímpar: "))

print(evenOrOdd(inputUser))
print(evenOrOdd(13))