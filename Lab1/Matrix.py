
class macierz:
    def __init__(self,argument,parametr = 0):  # konstruktor
        if isinstance(argument, tuple):
            wiersz, kolumna = argument
            self.macierz = [[parametr for i in range(kolumna)] for j in range(wiersz)]
        else:
            self.macierz = argument

    def size(self):
        return len(self.macierz), len(self.macierz[0])

    def __add__(self,other):
        if (self.size()[0] == other.size()[0]) and (self.size()[1] == other.size()[1]):     # Ta sama wielkosc
            wierszy = self.size()[0]
            kolumn = self.size()[1]

            add_result = [[0 for i in range(kolumn)] for j in range(wierszy)]

            for i in range(wierszy):
                for j in range(kolumn):
                    add_result[i][j] = self.macierz[i][j] + other.macierz[i][j]
            result = macierz(add_result)
            return result
        else:
            print("Nie da sie dodac macierzy")
            return None


    def __mul__(self,other):
        if (self.size()[1] == other.size()[0]):
            wierszy = self.size()[0]
            kolumn = other.size()[1]
            liczba_dodan = self.size()[1]

            mul_result = [[0 for i in range(kolumn)] for j in range(wierszy)]

            for i in range(wierszy):
                for j in range(liczba_dodan):
                    for k in range(kolumn):
                        mul_result[i][k] += self[i][j] * other[j][k]

            result = macierz(mul_result)
            return result
        else:
            print("Nie da sie przemnozyc macierzy")
            return None

    def __getitem__(self, item):
        return self.macierz[item]
    
    def __str__(self):
        wierszy = self.size()[0]
        kolumn = self.size()[1]
    
        string = ""
        for i in range(wierszy):
            for j in range(kolumn):
                string += str(self.macierz[i][j]) + " "
            string += "\n"
    
        return string



    def transpose(self):
        wierszy = self.size()[0]
        kolumn = self.size()[1]

        transpose_result = [[0 for i in range(wierszy)] for j in range(kolumn)]

        for i in range(wierszy):
            for j in range(kolumn):
                transpose_result[j][i] = self[i][j]
        result = macierz(transpose_result)
        return result


def wyznacznik2x2(macierz1 : macierz):
    return (macierz1[0][0]*macierz1[1][1])-(macierz1[0][1]*macierz1[1][0])

def Chio(mnoznik,macierz1 : macierz):

    wielkosc = macierz1.size()[0]

    if macierz1.size() == (2, 2):
        return  mnoznik * wyznacznik2x2(macierz1)
    
    elif macierz1[0][0] == 0:
        i = 0
        for i in range(wielkosc+1):
            if macierz1[i][0] != 0:

                macierz1[0][:], macierz1[i][:] = macierz1[i][:], macierz1[0][:]
                mnoznik *= -1
                break
    
    mnoznik2 = mnoznik * (1/(macierz1[0][0]**(wielkosc-2)))

    wynikowa = [[wyznacznik2x2(macierz([[macierz1[0][0], macierz1[0][j + 1]],
                                          [macierz1[i + 1][0], macierz1[i + 1][j + 1]]])) for j in range(macierz1.size()[0] - 1)] for i in range(wielkosc - 1)]
    return Chio(mnoznik2, macierz(wynikowa))

def Chio_Koniec(macierz1: macierz):
    return Chio(1,macierz1)






def main():
    matrix1 = macierz([[5, 1, 1, 2, 3],
                      [4, 2, 1, 7, 3],
                      [2, 1, 2, 4, 7],
                      [9, 1, 0, 7, 0],
                      [1, 4, 7, 2, 2]])

    result1 = Chio_Koniec(matrix1)
    print("Wyznacznik pierwszej macierzy:", result1)

    matrix2 = macierz([[0, 1, 1, 2, 3],
                      [4, 2, 1, 7, 3],
                      [2, 1, 2, 4, 7],
                      [9, 1, 0, 7, 0],
                      [1, 4, 7, 2, 2]])

    result2 = Chio_Koniec(matrix2)
    print("Wyznacznik drugiej macierzy:", result2)

if __name__ == "__main__":
    main()
    
    
    


