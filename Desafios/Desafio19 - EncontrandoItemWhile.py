fruta = (input("Adivinhe a fruta correta: ")).lower()

while fruta != "abacate":
    fruta = (input("Tente novamente, adivinhe a fruta correta: "))
    if fruta.lower() == "abacate":
        break

print("Parabéns, você acertou a fruta!!")
