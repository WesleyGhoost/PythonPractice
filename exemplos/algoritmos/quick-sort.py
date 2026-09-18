#Exemplo de quick-sort
def quick_sort(array):
    if len(array) == 0:
        return []

    pivot = array[0]

    smaller = []
    equal = []
    larger = []

    for number in array:
        if number < pivot:
            smaller.append(number)
        elif number == pivot:
            equal.append(number)
        else:
            larger.append(number)

    return quick_sort(smaller) + equal + quick_sort(larger)