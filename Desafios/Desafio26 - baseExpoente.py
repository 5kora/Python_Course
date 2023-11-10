def potencia(base, exp = 2):
    return base ** exp

inputBase = int(input(f'Digite a base desejada: '))
inputExp = int(input(f'Digite o expoente desejado: '))

print(f"Resultado completo {inputBase}^{inputExp}=  {potencia(inputBase,inputExp)}")
print(f"Resultado sem exp {inputBase}^?=  {potencia(inputBase)}")