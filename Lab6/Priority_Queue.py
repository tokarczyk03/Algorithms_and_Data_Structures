#nieskonczone

class Priority_Queue_Element:
    def __init__(self, data, priority):
        self.__dane = data
        self.__priority = priority

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __repr__(self):
        return f'{self.__priority} : {self.__dane}'
    

class Priority_Queue:

    def __init__(self):
        self.tab = []
        self.size = 0

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
        self.tab[0] = self.tab[self.size-1]
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


def main():

    queue = Priority_Queue()
    priorytety = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    dane = "GRYMOTYLA"

    for i in range(len(priorytety)):
        queue.enqueue(Priority_Queue_Element(dane[i],priorytety[i]))

    queue.print_tree(0,0)
    print()

    queue.print_tab()
    print()

    pierwszy = queue.dequeue()
    print(pierwszy)

    print(queue.peek())

    queue.print_tab()
    print()

    print(pierwszy)

    while not queue.is_empty():
        print(queue.dequeue())
    
    queue.print_tab()
    print()

main()



