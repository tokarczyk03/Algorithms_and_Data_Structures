
class Hash_Table():

    def __init__(self, size, c1 = 1, c2 = 0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def hash(self, key):

        if isinstance(key, str):
            hash_value = 0
            for i in key:
                hash_value = hash_value + ord(i)
            hash_value = hash_value % self.size
        else:
            hash_value = key % self.size
        return hash_value
    
    def search(self,key):

        for i in range(self.size):
            index = self.new_index(key,i)
            if self.tab[index] is not None and self.tab[index].key is key:
                return self.tab[index].data
        return None

    def insert(self,key,data):

        for i in range(self.size):
            index = self.new_index(key,i)
            if self.tab[index] is None:
                self.tab[index] = Element(key,data)
                return
            elif self.tab[index].key is key:
                self.tab[index].data = data
                return

        print("Brak miejsca")        
        return None


    def remove(self,key):
        for i in range(self.size):
            index = self.new_index(key,i)
            if self.tab[index].key is key and self.tab[index] is not None:
                self.tab[index] = None
                return
            if self.tab[index] is None:
                print("Brak danej")    
                return    
        return None

    def __str__(self):
        string = '['
        for i in range(self.size):
            string += f"{self.tab[i]}, "
        if string is not '[':
            string = string[:-2]
        string += "]"
        return string   

    def new_index(self,key,i):
        index = self.hash(key)
        return (index + self.c1 * i + self.c2 *i**2) % self.size




class Element():
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __equal__(self,other):
        if self.key == other.key:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.key}:{self.data}"
    
def test1(size, c1, c2):
    hashTable = Hash_Table(size, c1, c2)
    liczby = [1, 2, 3, 4, 5, 18, 31, 8, 9, 10, 11, 12, 13, 14 ,15]
    litery = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(15):
        hashTable.insert(liczby[i], litery[i])
        
    print(hashTable)
    print(hashTable.search(5))
    print(hashTable.search(14))
    hashTable.insert(5, 'Z')
    print(hashTable.search(5))
    hashTable.remove(5)
    print(hashTable)
    print(hashTable.search(31))
    hashTable.insert('test', 'W')
    print(hashTable)

def test2(size, c1, c2):
    hashTable = Hash_Table(size, c1, c2)
    litery = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(1, 16):
        hashTable.insert(13 * i, litery[i - 1])
    print(hashTable)

def main():
    test1(13, 1, 0)
    print()
    test2(13, 1, 0)
    print()
    test2(13, 0, 1)
    print()
    test1(13, 0, 1)
    print()

main()