#nieskonczone

def swapSort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


def shiftSort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j
        lista.insert(i, lista.pop(min_idx))
    return lista


data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]

print("Sortowanie przez wybieranie (swap):", swapSort(data.copy()))
print("Sortowanie przez wybieranie (shift):", shiftSort(data.copy()))

import random
import time

data = [random.randint(0, 99) for _ in range(10000)]

start = time.time()
swapSort(data.copy())
end = time.time()
print("Czas sortowania przez wybieranie (swap):", end - start)

start = time.time()
shiftSort(data.copy())
end = time.time()
print("Czas sortowania przez wybieranie (shift):", end - start)
    