paisCapital = {
'alemanha' : 'berlim',
'brasil' : 'brasília',
'bolívia' : 'sucre',
'suécia' : 'estocolmo',
'rússia' : 'moscou'
}

inputUser = input("Digite um país: ").lower()

if inputUser in paisCapital.keys():
    print(f"A capital de {inputUser} é {paisCapital[inputUser]}")
else:
    print("Desculpe, não temos informações sobre a capital desse país")