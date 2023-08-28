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

# # Atividade 46

# import math

# print(math.factorial(4))

####################################################################################################################################

# # Atividade 47

# cidades = ["Rio de Janeiro", "Parana", "Sao Paulo"]

# cidades[0] = "Santa Catarina"

# cidades.append("Amazonas")
# cidades.remove("Parana")
# print(cidades)

####################################################################################################################################

# # Atividade 50

# numeros = [1, 2, 3, 4, 5]

# letras = ["a", "b", "c"]

# final = numeros + letras

# numeros.extend(letras)

# print(final)
# print(numeros)

# itens = [["item1","item2"],["item3","item4"]]

# print(itens[0][1])

####################################################################################################################################

# # Atividade 51

# produtos = ["arroz", "feijao", "laranja", "banana",1,2,3,4]

# item1,item2,item3,*outros = produtos

# print(item1)
# print(item2)
# print(item3)
# print(outros)

####################################################################################################################################

# # Atividade 52

# valores = [1,2,3,4,5]

# for numero in valores:
#     print(numero)

    
####################################################################################################################################

# # Atividade 53

# corDesejada = input("Digite a cor desejada: ").lower()

# cores = ["amarelo", "verde", "azul","vermelho"]

# if corDesejada in cores:
#     print("Em estoque!")
# else:
#     print("Cor não disponivel em estoque!")

####################################################################################################################################

# # Atividade 54

# cores = ["amarelo", "verde", "azul","vermelho"]
# valores = [10, 20, 30, 40]

# lista = list('comprar')

# print(lista)

# duasListas = zip(cores,valores)

# print(list(duasListas))

####################################################################################################################################

# # Atividade 55

# frutasUsuario = input("Digite o nome das frutas separados por virgula: ")

# print(frutasUsuario.split(","))

####################################################################################################################################

# # Atividade 56

# coresLista = ["amarelo", "verde", "azul","vermelho"]
# coresTuple = ("amarelo", "verde", "azul","vermelho")

# print(type(coresLista))
# print(type(coresTuple))


# coresLista.append("123") #OK
# # coresTuple.append("123") #NOK


####################################################################################################################################
# from array import array

# # Atividade 57

# letras = ["a", "b", "c", "d"]

# numerosInt = [1, 2, 3, 4]

# numerosFloat = [1.1, 2.2, 3.3, 4.4]

# print(letras)
# print(numerosInt)
# print(numerosFloat)

# letras = array("u", ["a", "b", "c", "d"])
# numerosInt = array("i", [1, 2, 3, 4])
# numerosFloat = array("f", [1.1, 2.2, 3.3, 4.4])

# print(letras)
# print(numerosInt)
# print(numerosFloat)

####################################################################################################################################

# # Atividade 58

# list1 = [10, 20, 30, 40, 50]
# list2 = [10, 20, 60, 70]

# num1 = set(list1)
# num2 = set(list2)

# print(num1 | num2) # Union
# print(num1 - num2) # Difference
# print(num1 ^ num2) # Symmetric Difference
# print(num1 & num2) # And

# print(len(num1))
# #print(num1[0]) # Index perdido

####################################################################################################################################

# # Atividade 59

# list1 = set([1, 2, 3, 4, 5, 6])
# s1 = {1, 2, 3, 5, 6}
# s1.add(9)
# s1.update([11,12,13,14])
# s1.remove(9)
# s1.discard(90)

# print(list1)
# print(s1)

####################################################################################################################################

# # Atividade 60

# set1 = {'a', 'b', 'c'}
# set2 = {'a', 'd', 'e'}
# set3 = {'c', 'd', 'f'}

# set4 = set1.union(set2)

# print(set4)

# set5 = set1.difference(set3)

# print(set5)

# set6 = set1.intersection(set2)

# print(set6)

# set7 = set1.symmetric_difference(set3)

# print(set7)

####################################################################################################################################

# # Atividade 61

# aluno = {"nome" : "Ana", "idade" : 16, "notaFinal" : "A", "aprovação" : True}

# print(aluno)
# print(aluno["idade"])

# aluno["nome"] = "João"
# print(aluno)

# aluno.update({"nome" : "Zeca", "notaFinal" : "B"})
# print(aluno)

# aluno.update({"endereco" : "Rua B"})
# print(aluno)

# print(aluno.get('cpf', "Key inexistente"))

# del aluno["endereco"]

# print(aluno)

####################################################################################################################################

# # Atividade 62
# aluno = {"nome" : "Ana", "idade" : 16, "notaFinal" : "A", "aprovação" : True}

# for x in aluno.keys():
#     print(x)

# print("************************")

# for x in aluno.values():
#     print(x)

# print("************************")

# for x in aluno.items():
#     print(x)

# print("************************")
    
# for keys, values in aluno.items():
#     print(f'[{keys},{values}]')

####################################################################################################################################

# # Atividade 63

# aluno = {
#     "nome" : "Ana",
#     "idade" : 16,
#     "notaFinal" : "A",
#     "aprovação" : True,
#     "materias" : ["ingles", "matematica", "programação"]
#     }

# print(aluno)
# print(aluno.get("materias"))
# print(len(aluno))

####################################################################################################################################

# # Atividade 65

# somar10 = lambda x: x + 10

# print(somar10(2))

####################################################################################################################################

# # Atividade 66

# def somar(x):
#     func2 = lambda x: x + 10
#     return func2(x) * 4

# print(somar(2))

####################################################################################################################################

# # Atividade 67

# lista1 = [1, 2, 3, 4]

# def multi(x):
#     return x * 2

# print(multi(2))

# lista2 = map(multi, lista1)

# print(list(lista2))

####################################################################################################################################

# # Atividade 68

# lista1 = [1, 2, 3, 4]

# # lista2 = map(lambda x : x * 2, lista1)

# print(list(map(lambda x : x * 2, lista1)))

####################################################################################################################################

# # Atividade 69

# valores = [10, 12, 34, 44, 57]

# def remover20(x):
#     return x > 20

# resultado = list(filter(remover20, valores))

# print(resultado)

# print(list(filter(lambda x: x > 20, valores)))

####################################################################################################################################

# # Atividade 70

# frutas1 = ["abacate", "banana", "morango", "kiwi", "abacaxi"]
# frutas2 = []

# for item in frutas1:
#     if 'b' in item:
#         frutas2.append(item)

# print(frutas2)

# frutas3 = [item for item in frutas1 if 'n' in item]

# print(frutas3)

####################################################################################################################################

# # Atividade 71

# valores = []

# for x in range(6):
#     valores.append(x * 10)

# print(valores)

# valores2 = [x * 10 for x in range(6)]

# print(valores)

####################################################################################################################################

# Atividade 72

from sys import getsizeof

numeros = [x * 10 for x in range(1000)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print("************************")

numeros = (x * 10 for x in range(1000))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))
