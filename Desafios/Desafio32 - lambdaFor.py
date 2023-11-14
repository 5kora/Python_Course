squareValue = lambda x : x ** 2

squareList = [1, 2, 3, 4, 5, 6, 8, 9]

for num in squareList:
    result = squareValue(num)
    print(f'O valor de {num}^2 é: {result}')