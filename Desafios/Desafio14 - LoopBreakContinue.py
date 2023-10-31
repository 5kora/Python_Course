print("Primeiro loop:")

for x in range(1,11):
    if x > 5:
        break
    print(x)

print("Segundo loop:")

for x in range(1,11):
    if x == 5:
        continue
    print(x)
    