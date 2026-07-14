numbersList = [1, 2, 3, 4, 5, 6]
anotherList = [10, 20, 30, 40]

numbersList.append(7)
print(numbersList)

numbersList.extend(anotherList)
print(numbersList)

numbersList.insert(7, 8)
print(numbersList)

numbersList.remove(40)
print(numbersList)

numbersList.pop(3)
print(numbersList)

anotherList.clear()
print(anotherList)


listaBaguncada = [3, 3, 62, 65, 1, 5, 20]
listaBaguncada.sort()
print(listaBaguncada)

listaBaguncada2 = [76, 3, 8, 9, 19, 43, 89]
listaArrumada = sorted(listaBaguncada2)
print(listaArrumada)

listaArrumada.reverse()
print(listaArrumada)

indexLista = listaArrumada.index(43)
print(indexLista)
