import heapq

#Prioridade por valores
my_heap = []
heapq.heappush(my_heap, 10)
print(heapq.heappop(my_heap))


#Prioridade por nivel de propriedade
my_heap_2 = []
heapq.heappush(my_heap_2, (3, 'A'))
heapq.heappush(my_heap_2, (2, 'B'))
heapq.heappush(my_heap_2, (1, 'C'))
print(heapq.heappop(my_heap_2))