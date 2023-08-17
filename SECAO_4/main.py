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

#Atividade 17
import datetime
from datetime import datetime

anoNascimento = input("Digite o seu ano de nascimento (XXXX): ")
idade = str(int(datetime.now().year) - int(anoNascimento))

print("A idade é: " + idade)

