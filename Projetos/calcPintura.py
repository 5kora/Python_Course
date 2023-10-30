rendimento = int(input('Qual é o rendimento da lata em m²? '))
largura = int(input('Qual é a largura da parede m? '))
altura = int(input('Qual é a altura da parede m? '))

def calculoTinta():
    totalLatas = (largura * altura) / rendimento
    print(f'Voce precisa de {totalLatas} latas de tinta')

calculoTinta()