estoque = ['BMW X6', 'BMW i5', 'BMW i8']
estoque = list(map(str.upper,estoque))
userInput = str(input("Digite o carro que deseja comprar: ")).upper()

if userInput in estoque:
    print("Este carro está disponível.")
else:
    print("Desculpe, este carro não está disponível.")