# exemplo 1 - range
for n in range(20, 5, -2):
    print(n)


# exemplo 2 - for in
listaNumeros = [5, 7, 10, 56, 2]
somaNumero = 0

for num in listaNumeros:
    somaNumero += num

print(somaNumero)


# exemplo 3 - loop aninhado
categorias = ['Fruta', 'Vegetal']
frutas = ['Maçã', 'Cenoura', 'Laranja']

for categoria in categorias:
    for fruta in frutas:
        print(categoria, fruta)


# exemplo 4 - while
valor = 0

while valor < 4:
    valor += 1
    print(valor)


# exemplo 5 - loop aninhado + if break
palavras = ['Caderno' , 'Chifre', 'Giz', 'Cabelo', 'Amar']

for palavra in palavras:
    for letra in palavra:
        if letra in 'aeiou':
            print(f"A palavra '{palavra}' possui vogal")
            break
    else:
        print(f"A palavra '{palavra}' não possui vogal")


# exemplo 6 - list
novaListaNumeros = list(range(3, 31, 3))
print(novaListaNumeros)


# exemplo 7 - enumerate
listaPaises = ['Espanha', 'França', 'Brasil', 'Alemanha', 'Japão']
print(list(enumerate(listaPaises, 1)))


# exemplo 8 - zip
listaPaises2 = ['Russia', 'China', 'Noruega', 'Chile', 'Canadá']
IDs = [1, 2, 3, 4, 5]

for pais, id in zip(listaPaises2, IDs):
    print(f"País: {pais}, ID: {id}")


# exemplo 9 - list comprehention
par_ou_impar_numeros = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in range(21)]
print(par_ou_impar_numeros)


# exemplo 10 - filter
palavras = ['Mapa', 'Cachorro', 'Sucesso', 'Califórnia', 'Museu', 'Gato']

def palavrasLongas(palavra):
    return len(palavra) > 4

encontrarPalavrasLongas = list(filter(palavrasLongas, palavras))
print(encontrarPalavrasLongas)


# exemplo 11 - map
celsius = [10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)


# exemplo 12 - sum
listaNumeros2 = [4, 7, 10, 65, 22]

sumNumbers = sum(listaNumeros2, 17)
print(sumNumbers)


# exemplo 13 - lambda
listaNumeros3 = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, listaNumeros3))
print(even_numbers)