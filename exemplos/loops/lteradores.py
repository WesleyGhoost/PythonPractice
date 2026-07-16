# exemplo 1
for n in range(20, 5, -2):
    print(n)


# exemplo 2
listaNumeros = [5, 7, 10, 56, 2]
somaNumero = 0

for num in listaNumeros:
    somaNumero += num

print(somaNumero)


# exemplo 3
categorias = ['Fruta', 'Vegetal']
frutas = ['Maçã', 'Cenoura', 'Laranja']

for categoria in categorias:
    for fruta in frutas:
        print(categoria, fruta)


# exemplo 4
valor = 0

while valor < 4:
    valor += 1
    print(valor)


# exemplo 5
palavras = ['Caderno' , 'Chifre', 'Giz', 'Cabelo', 'Amar']

for palavra in palavras:
    for letra in palavra:
        if letra in 'aeiou':
            print(f"A palavra '{palavra}' possui vogal")
            break
    else:
        print(f"A palavra '{palavra}' não possui vogal")


# exemplo 6
novaListaNumeros = list(range(3, 31, 3))
print(novaListaNumeros)

# exemplo 7
listaPaises = ['Espanha', 'França', 'Brasil', 'Alemanha', 'Japão']
print(list(enumerate(listaPaises, 1)))


# exemplo 8
listaPaises2 = ['Russia', 'China', 'Noruega', 'Chile', 'Canadá']
IDs = [1, 2, 3, 4, 5]

for pais, id in zip(listaPaises2, IDs):
    print(f"País: {pais}, ID: {id}")