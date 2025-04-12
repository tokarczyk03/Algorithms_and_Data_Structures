

class Queue():
    def __init__(self, size = 5):
        self.tab = [None for i in range(size)]
        self.size = size
        self.saveID = 0
        self.readID = 0

    def is_empty(self):
        if self.saveID == self.readID:
            return True
        else:
            return False
        
    def peek(self):
        if self.saveID == self.readID:
            return None
        else:
            return self.tab[self.readID]
        
    def dequeue(self):
        if self.saveID == self.readID:
            return None
        else:
            return_data = self.tab[self.readID]
            self.tab[self.readID] = None

            if self.readID == (len(self.tab)-1):
                self.readID = 0
            else:
                self.readID = self.readID + 1
            return return_data
        
    def enqueue(self, data):
        self.tab[self.saveID] = data
        if self.saveID < self.size-1:
                self.saveID += 1

        else:
            self.saveID == self.size
            self.saveID = 0

        if self.saveID == self.readID:
            self.tab  = self.realloc(self.tab, self.size*2)

            odleglosc = len(self.tab) - len(self.tab[self.saveID:self.size])
            self.tab[odleglosc:] = self.tab[self.readID:self.size]
            for i in range(self.readID,self.size):
                self.tab[i] = None
            self.readID = odleglosc
            self.size *= 2


    def __str__(self):
        string = '['
        i = self.readID
        while i is not self.saveID:
            string += str(self.tab[i]) + ', '
            if i < self.size - 1:
                i += 1
            else:
                i = 0
        if string != '[':
            string = string[:-2]
        string += ']'
        return string
    
    def getTab(self):
        return self.tab

    def realloc(self,tab, size):
        oldSize = len(self.tab)
        return [tab[i] if i<oldSize else None  for i in range(size)]
    


def main():
    
    queue = Queue()
    for i in range(1,5):
        queue.enqueue(i)
    print(queue.dequeue())
    print(queue.peek())
    print(queue)
    for i in range(5,9):
        queue.enqueue(i)
    print(queue.getTab())
    while(not queue.is_empty()):
        print(queue.dequeue())
    print(queue)

main()