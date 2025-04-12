
class Element():

    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev




class SingleLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None


    def destroy(self):
        current = self.head
        while current:
            next_node = current.next
            del current
            current = next_node
        self.head = None
        self.tail = None


    def add(self,data):
        new_element = Element(data, self.head)
        if self.head:
            self.head.prev = new_element
        else:
            self.tail = new_element
        self.head = new_element
        



    def append(self,data):
        new_element = Element(data, None, self.tail)
        if self.tail:
            self.tail.next = new_element
        else:
            self.head = new_element
        self.tail = new_element


    def remove(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

    def remove_end(self):
        if self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None


    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        if self.head is None:
            return  0
        else:
            current_element = self.head
            i = 1
            while(current_element.next):
                current_element = current_element.next
                i += 1
            return i
    
    def get(self):
        return self.head.data
    
    def __str__(self):
        element = self.head
        string = ''
        if self.head != None:
            while element != None:
                string += '-> ' + str(element.data) + '\n'
                element = element.next
        return string
    

def main():
    universities = [
        ('AGH', 'Kraków', 1919),
        ('UJ', 'Kraków', 1364),
        ('PW', 'Warszawa', 1915),
        ('UW', 'Warszawa', 1915),
        ('UP', 'Poznań', 1919),
        ('PG', 'Gdańsk', 1945)]

    uczelnie = SingleLinkedList()
    for i in range(3):
        uczelnie.append(universities[i])
    for i in range(3,6):
        uczelnie.add(universities[i])
    print(uczelnie)
    print(uczelnie.length())
    print()
    uczelnie.remove()
    print(uczelnie.get())
    print()
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.append(universities[0])
    uczelnie.remove_end()
    print(uczelnie)
    print(uczelnie.is_empty())

main()