#for n in range(20, 5, -2):
#   print(n)


qtd = 0
soma = 0
media = 0
valor = float(input('Digite um valor:'))

while valor > 0.0:
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input('Digite um valor:'))

media = soma / qtd

print("Total dos valores: ", soma)
print("Quantidade: ", qtd)
print("Média dos valores: ", media)