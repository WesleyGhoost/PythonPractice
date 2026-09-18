#Exemplo de selection-sort
def selection_sort(array):
    for i in range(len(array)):
        menor = i

        for j in range(i + 1, len(array)):
            if array[j] < array[menor]:
                menor = j

        if menor != i:
            array[i], array[menor] = array[menor], array[i]

    return array