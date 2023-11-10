inputUser = int(input('Digite um numero para receber o valor ao cubo: '))

calcCube = lambda x : x ** 3

print(f'O resultado de {inputUser}^3 é: {calcCube(inputUser)}')