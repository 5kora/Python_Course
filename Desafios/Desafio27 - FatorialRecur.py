def fatorial(num):
    if num == 0:
        return 1
    return num * fatorial(num -1)

inputUser = int(input("Digite o numero que deseja saber o fatorial: "))

resultado = fatorial(inputUser)

print(f'O fatorial de {inputUser} é: {resultado}')