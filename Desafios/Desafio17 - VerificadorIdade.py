idade = int(input("Digite sua idade: "))

if idade < 13:
    print("Voce é uma criança")
elif idade >= 13 and idade < 19:
    print("Voce é um adolescente!")
elif idade > 20:
    print("Voce é um adulto!")