nota1 = int(input("Digite sua primeira nota:"))
nota2 = int(input("Digite sua segunda nota:"))

media = (nota1 + nota2) / 2

print(media)

if media >= 6 and media < 10:
    print("Aprovado")
elif media == 10:
    print("Nota Perfeita!")
else:
    print("Reprovado")