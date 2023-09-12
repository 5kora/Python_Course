funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turnoDia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turnoNoite = ['Pedro', 'Sophia', 'Bruno']
temCarro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#Funcionarios que tem carro e trabalham a noite
Lista1 = set(funcionarios).intersection(set(temCarro))