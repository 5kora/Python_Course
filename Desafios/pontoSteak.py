# 48 - RARE, 54 - Medium Rare, 60 - Medium, 65- Medium Well, 71- Well Done
#Cozinhar por mais alguns minutos
#Bem passada!
def pointSteak(tempCelcius):
    if(tempCelcius < 49):
        print('Boi berrando!')
    elif(tempCelcius > 49 and tempCelcius < 55):
        print('Rare (Selada)')
    elif(tempCelcius > 54 and tempCelcius < 60):
        print('Medium Rare (Ao ponto para mal)')
    elif(tempCelcius > 60 and tempCelcius < 65):
        print('Medium (Ao ponto)')
    elif(tempCelcius > 65 and tempCelcius < 71):
        print('Medium Well (Ao ponto para bem passada)')
    else:
        print('Virou carvão!')

temperaturaCarne = int(input("Digite a temperatura em Celsius da sua carne: "))

pointSteak(temperaturaCarne)