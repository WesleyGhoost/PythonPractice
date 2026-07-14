listaFrutas = ['Maçã', 'Laranja', 'Uva', 'Melancia', ['Limão', 'Manga', 'Melão']]

print(len(listaFrutas))

print(listaFrutas[2])
print(listaFrutas[0])
print(listaFrutas[4][1])

del listaFrutas[3]
print(listaFrutas)

print(listaFrutas[1::2])

vermelha, laranja, roxa, resto = listaFrutas

print(vermelha)
print(laranja)
print(roxa)
print(resto)

nome = 'Claudio'
print(list(nome))