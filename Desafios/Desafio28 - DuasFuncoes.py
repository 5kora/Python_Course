def doubleValue(value):
    return 2 * value

def squareValue(value):
    return value ** 2

inputUser = int(input('Digite um numero para calcular o quadrado do dobro: '))

result = squareValue(doubleValue(inputUser))

print(f'O resultado para o valor {inputUser} é: {result}')