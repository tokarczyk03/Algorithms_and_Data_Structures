
import random
import time

def insertionSort(list):
    for i in range(len(list)):
        temp = list[i]
        j = i-1
        while j >=0 and temp < list[j] :
                list[j+1] = list[j]
                j -= 1
        list[j+1] = temp
    return list

def shellSort(list):
    n = len(list)
    h = n//2
    while h > 0:
        for i in range(h,n):
            temp = list[i]
            j = i
            while  j >= h and temp < list[j-h] :
                list[j] = list[j-h]
                j -= h
            list[j] = temp
        h //= 2
    return list



def main():
    data11 = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    print("Sortowanie insertion sort:", insertionSort(data11))

    data12 = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    print("Sortowanie Shell sort:", shellSort(data12))

    data2 = [random.randint(0, 99) for _ in range(10000)]
    t_start = time.perf_counter()
    insertionSort(data2)
    t_stop = time.perf_counter()
    print("Czas sortowania insertion sort:", t_stop - t_start)

    data3 = [random.randint(0, 99) for _ in range(10000)]
    t_start = time.perf_counter()
    shellSort(data3)
    t_stop = time.perf_counter()
    print("Czas sortowania Shell sort:", t_stop - t_start)


main()
