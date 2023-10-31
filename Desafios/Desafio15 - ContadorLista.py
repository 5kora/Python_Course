frutas = ["mAça", "banana", "maçA", "manga", "uva", "maça", "abacaxi"]
contador = 0

for x in frutas:
    if x.lower() == "maça":
        contador +=1

print(f'Minha cesta de frutas tem {contador} maças!')