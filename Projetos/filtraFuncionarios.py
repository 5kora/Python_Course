funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turnoDia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turnoNoite = ['Pedro', 'Sophia', 'Bruno']
temCarro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#Funcionarios que tem carro e trabalham a noite
lista1 = set(temCarro).intersection(set(turnoNoite))

#Funcionarios que tem carro e trabalham durante o dia
lista2 = set(temCarro).intersection(set(turnoDia))

#Funcionarios que não tem carro
lista3 = set(temCarro).symmetric_difference(funcionarios)

print(f'Funcionarios que tem carro e trabalham a noite: {lista1}')
print(f'Funcionarios que tem carro e trabalham durante o dia: {lista2}')
print(f'Funcionarios que não tem carro: {lista3}')
