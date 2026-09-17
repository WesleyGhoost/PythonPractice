# Exemplo de Busca Linear:
def linear_search(arr, target):
    for i in arr:
        if i == target:
            return i
    return -1

print(linear_search([2, 6, 4, 10,], 6))



#Exemplo de Busca Binária:
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([5, 3, 12, 7, 20], 12))