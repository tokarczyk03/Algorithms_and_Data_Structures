#skonczone
import random
import time

class Priority_Queue_Element:
    def __init__(self, priority, data):
        self.__dane = data
        self.__priority = priority

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __repr__(self):
        return f'{self.__priority} : {self.__dane}'
    

class Priority_Queue:

    def __init__(self, parametr = None):
        if parametr == None:
            self.tab = []
            self.size = 0
        else:
            self.tab = parametr
            self.size = len(parametr)
            for i in range(self.parent(self.size-1),-1,-1):
                self.heapify_down(i)

    def is_empty(self):
        return self.size == 0
    
    def left(self, ID):
        return 2 * ID + 1
    
    def right(self, ID):
        return 2 * ID + 2
    
    def parent(self, ID):
        return (ID - 1) // 2
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0]

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.tab[0]
        self.tab[0], self.tab[self.size-1]  = self.tab[self.size-1], self.tab[0]
        self.size -= 1
        self.heapify_down(0)
        return data

    def enqueue(self,element):
        if self.size < len(self.tab):
            self.tab[self.size] = element
        elif self.size == len(self.tab):
            self.tab.append(element)

        self.size += 1
        self.heapify_up(self.size-1)


    def heapify_down(self, ID):
        left = self.left(ID)
        right = self.right(ID)
        largest = ID

        if left < self.size and self.tab[left] > self.tab[largest]:
            largest = left

        if right < self.size and self.tab[right] > self.tab[largest]:
            largest = right

        if largest != ID:
            self.tab[ID], self.tab[largest] = self.tab[largest], self.tab[ID]
            self.heapify_down(largest)
    
    def heapify_up(self, ID):

        while ID != 0 and self.tab[self.parent(ID)] < self.tab[ID]:
            self.tab[self.parent(ID)], self.tab[ID] = self.tab[ID], self.tab[self.parent(ID)]
            ID = self.parent(ID)


    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)



def swapSort(lista):
    for i in range(len(lista)):
        swapID = i
        for j in range(i+1, len(lista)):
            if lista[swapID] > lista[j]:
                swapID = j
        lista[i], lista[swapID] = lista[swapID], lista[i]
    return lista


def shiftSort(lista):
    for i in range(len(lista)):
        swapID = i
        for j in range(i+1, len(lista)):
            if lista[swapID] > lista[j]:
                swapID = j
        lista.insert(i, lista.pop(swapID))
    return lista

def main():

    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    lista1  = [ Priority_Queue_Element(key, value) for key,value in  data]
    queue = Priority_Queue(lista1)

    queue.print_tab()
    queue.print_tree(0,0)
    while not queue.is_empty():
        queue.dequeue()
    print(lista1)

    ####

    lista2 = []
    for i in range(10000):
        lista2.append(random.randrange(0,99))

    t_start = time.perf_counter()

    lista21 = Priority_Queue(lista2)
    while not lista21.is_empty():
        lista21.dequeue()
    
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


    print("Sortowanie SwapSort:", swapSort(data.copy()))
    print("Sortowanie ShiftSort:", shiftSort(data.copy()))

    t_start = time.perf_counter()
    swapSort(lista2.copy())
    t_stop = time.perf_counter()
    print("Czas obliczeń SwapSort:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    shiftSort(lista2.copy())
    t_stop = time.perf_counter()
    print("Czas obliczeń ShiftSort:", "{:.7f}".format(t_stop - t_start))

main()



