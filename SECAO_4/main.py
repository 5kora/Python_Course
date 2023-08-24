# # Atividade 14
# x = str(3)
# y = int(4)
# z = float(5)

# print(x + x)
# print(y + y)
# print(z + z)

# ####################################################################################################################################

# # O marcos tem 26 anos de idade e mora em Pinhais
# idade  = input('Digite sua idade: ')
# idade = str(idade)
# nome = input("Digite seu nome: ")
# cidade = input("Digite sua cidade: ")

# print("O " + nome + "tem " + idade + " anos de idade e mora em " + cidade)

####################################################################################################################################

# #Atividade 17
# import datetime
# from datetime import datetime

# anoNascimento = input("Digite o seu ano de nascimento (XXXX): ")
# idade = str(int(datetime.now().year) - int(anoNascimento))

# print("A idade é: " + idade + " anos.")

####################################################################################################################################

# # Atividade 18

# fruta  = "Abacate"
# numero = str(99.58)

# # index
# print(fruta[2:5])
# print(fruta[2])
# print(fruta[-1])

# print(numero.split(".")[1])

####################################################################################################################################

# # Atividade 19

# # Dolly guarana, saboroso e [delicioso]

# refrigerante = "Dolly"
# sabor = "guarana"
# adjetivo = "delicioso"

# texto = f'{refrigerante} {sabor}, saboroso e [{adjetivo}]'

# print(texto)

####################################################################################################################################

# # Atividade 20

# mensagem = "     Eu amo pizza de chocolate"

# # Lowercase
# print(mensagem.lower())
# # Uppercase
# print(mensagem.upper())
# # Capitalize (ja esta assim a minha frase)
# print(mensagem.capitalize())
# # find letter (Se não encontrar retorna -1)
# print(mensagem.find("a"))
# #replace method
# print(mensagem.replace("a","i"))
# #strip method
# print(mensagem.strip())


####################################################################################################################################

# # Atividade 24

# velocidade = 35

# if velocidade > 80:
#     print("Acima da média patrao!")
# elif velocidade < 80 and velocidade > 40 :
#     print("Niceee")
# else:
#     print("Lerdinho hehehe")
    
# print("Fim!")

####################################################################################################################################

# # Atividade 25

# rendaAcima5k = True

# nomeLimpo = True

# if rendaAcima5k and nomeLimpo:
#     print("Financiamento aprovado!")
# else:
#     print("Financiamento negado!")

####################################################################################################################################

# # Atividade 27

# for numero in range(5):
#     print(numero + 1)

# print("*******************")

# for numero in range(1, 6):
#     print(numero)

# print("*******************")

# for numero in range(1, 10, 2):
#     print(numero)

####################################################################################################################################

# # Atividade 28
# palavra = "Dollynho".lower()

# for letra in palavra :
#     print(f'{letra} esta dentro da palvra {palavra}')

####################################################################################################################################

# # Atividade 29
# compraConfirmada = True
# dadosCompra = "Compra no valor de R$12,50 e entrega confirmada"

# for enviar in range(3):
#     if compraConfirmada:
#         print(dadosCompra)
#         print("Detalhes enviados para o seu email")
#         break
#     else:
#         print("Falha na compra")

####################################################################################################################################

# # Atividade 30

# for numero1 in range(5):
#     print(f'Produto: {numero1}')
#     for numero2 in range(5):
#         print(f'Subitem do produto {numero1}: {numero2}')
        
####################################################################################################################################

# # Atividade 31

# palavra = 'FANTASTICO'

# for space in palavra:
#     print(f'{space} ', end="" )

####################################################################################################################################

# # Atividade 32

# linhas = input("Digite a quantidade de linhas desejadas: ")
# colunas = input("Digite a quantidade de colunas desejadas: ")
# simbolo = '#'

# for l in range(int(linhas)):
#     for c in range(int(colunas)):
#         print(simbolo, end="")
#     print("")

####################################################################################################################################

# # Atividade 33

# valor = 100
# dia = 0

# while valor > 20:
#     dia+=1
#     print(f'No dia {dia} o produto vai ser vendido por: ')
#     print(f'R${valor}')
#     valor -= 5

####################################################################################################################################

# # Atividade 34

# idade = 15

# podeVotar = 'Voto permitido' if idade >= 16 else 'Voto não permitido!'

# print(podeVotar)

####################################################################################################################################

# # Atividade 36

# valor = int(input("Digite o valor do seu produto: R$"))

# while valor > 20:
#     print(f'O seu produto sera vendido por: R$ {valor * 1.1}')
#     break

####################################################################################################################################

# # Atividade 39

# def firstFunction():
#     print("Essa é minha primeira funcao em python!!")

# firstFunction()

####################################################################################################################################

# # Atividade 40

# numero1 = int(input(f'Digite o primeiro numero: '))
# numero2 = int(input(f'Digite o segundo numero: '))

# def somaNumeros(num1, num2):
#     return num1 + num2

# resultado = somaNumeros(numero1, numero2)

# print(resultado)

####################################################################################################################################

# # Atividade 41

# def boasVindas(nome, quantidade = 6):
#     print(f'Olá {nome}')
#     print(f'Temos {str(quantidade)} garrafas em estoque')

# boasVindas("Dolynho")


####################################################################################################################################

# # Atividade 43

# def cliente1(nome):
#     print(f'Olá {nome}')

    
# def cliente2(nome):
#     return f'Olá {nome}'


####################################################################################################################################

# # Atividade 44

# def soma(*numeros):
#     resultado = 0
#     for numero in numeros:
#         resultado += numero
#     return resultado

# resultado = soma(2,3,4,5,6)

# print(resultado)

# ####################################################################################################################################

# # Atividade 45

# def agencia(**carro):
#     return carro

# print(agencia(marca = "BMW", cor = "Branco", motor="2.0"))

####################################################################################################################################

# Atividade 46

import math

print(math.factorial(4))
