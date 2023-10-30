altura = float(input("Qual é a sua altura em cm: "))
peso = float(input("Qual é seu pego em kg: "))

imc = peso / (altura/100) ** 2

print(imc)

if imc < 18.5:
    print("Tu esta na MAGREZA irmão!")
elif imc >= 18.5  and imc < 24.9:
    print("Tu esta NORMAL irmão!")
elif imc >= 25 and imc < 29.9 :
    print("Tu esta SOBREPESO irmão!")
elif imc >= 30 and imc < 39.9 :
    print("Tu esta OBESIDADE irmão!")
elif imc > 40:
    print("Tu esta em OBESIDADE GRAVE irmão!")