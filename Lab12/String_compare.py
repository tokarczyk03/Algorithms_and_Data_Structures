#skonczone
import numpy as np


#  a)
def string_compare(P : str, T : str, i =  None, j = None):
    if i is None and j is None:
        i = len(P) - 1
        j= len(T) - 1

    if i == 0:
        return j
    if j == 0:
        return i
    
    changes = string_compare(P,T,i-1,j-1) + (P[i] != T[j])
    inserts = string_compare(P,T,i,j-1) + 1
    deletes = string_compare(P,T,i-1,j) + 1

    less_cost = min(changes,inserts,deletes)

    return less_cost

#  b)
def string_compare_pd(P : str, T : str):
    m, n = len(P), len(T)
    

    D = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        D[i][0] = i
    for j in range(n+1):
        D[0][j] = j

    parents = [['X' for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        parents[i][0] = 'D'
    for j in range(1, n+1):
        parents[0][j] = 'I'

    for i in range(1, m+1):
        for j in range(1, n+1):
            changes = D[i-1][j-1] + (P[i-1] != T[j-1])
            inserts = D[i][j-1] + 1
            deletes = D[i-1][j] + 1

            min_cost = min(changes, inserts, deletes)
            D[i][j] = min_cost

            if min_cost == changes:
                parents[i][j] = 'S' if P[i-1] != T[j-1] else 'M'
            elif min_cost == inserts:
                parents[i][j] = 'I'
            else:
                parents[i][j] = 'D'
    return D[m][n]

#  c)
def string_compare_pd_path(P: str, T: str):
    m, n = len(P), len(T)
    
    D = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        D[i][0] = i
    for j in range(n+1):
        D[0][j] = j

    parents = [['X' for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        parents[i][0] = 'D'
    for j in range(1, n + 1):
        parents[0][j] = 'I'

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            changes = D[i - 1][j - 1] + (P[i - 1] != T[j - 1])
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1

            min_cost = min(changes, inserts, deletes)
            D[i][j] = min_cost

            if min_cost == changes:
                parents[i][j] = 'S' if P[i - 1] != T[j - 1] else 'M'
            elif min_cost == inserts:
                parents[i][j] = 'I'
            else:
                parents[i][j] = 'D'
    
    i, j = m, n
    operations = []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and (parents[i][j] == 'M' or parents[i][j] == 'S'):
            if not (parents[i][j] == 'M' and i == 1 and j == 1):
                operations.append(parents[i][j])
            i -= 1
            j -= 1
        elif j > 0 and parents[i][j] == 'I':
            operations.append('I')
            j -= 1
        elif i > 0 and parents[i][j] == 'D':
            operations.append('D')
            i -= 1
        else:
            break

    operations = operations[::-1]
    path = ''.join(operations)

    return path


#  d)
def string_compare_pd_conect(P : str, T : str):
    m, n = len(P), len(T)
    

    D = np.zeros((m, n))
    for i in range(m):
        D[i][0] = i
    for j in range(n):
        D[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            changes = D[i-1][j-1] + (P[i-1] != T[j-1])
            inserts = D[i][j-1] + 1
            deletes = D[i-1][j] + 1

            min_cost = min(changes, inserts, deletes)
            D[i][j] = min_cost

    min_value = float('inf')
    for i in range(n):
        if D[m - 1][i] < min_value:
            min_value = D[m - 1][i]
            index = i - m + 2

    return index


#  e)
def string_compare_pd_longest_subsequence(P, T):
    m = len(P)
    n = len(T)
    D = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if P[i-1] == T[j-1] and P[i-1] != ' ':
                D[i][j] = D[i-1][j-1] + 1
            else:
                D[i][j] = max(D[i-1][j], D[i][j-1])

    longest_sub = ''
    i, j = m, n
    while i > 0 and j > 0:
        if P[i-1] == T[j-1] and P[i-1] != ' ':
            longest_sub = P[i-1] + longest_sub
            i -= 1
            j -= 1
        elif D[i-1][j] > D[i][j-1]:
            i -= 1
        else:
            j -= 1
    return longest_sub

#  f)
def string_compare_pd_mono(P, T):
    m = len(P)
    n = len(T)
    D = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if P[i-1] == T[j-1] and P[i-1] != ' ':
                D[i][j] = D[i-1][j-1] + 1
            else:
                D[i][j] = max(D[i-1][j], D[i][j-1])
    
    lcs = ''
    i, j = m, n
    while i > 0 and j > 0:
        if P[i-1] == T[j-1] and P[i-1] != ' ':
            lcs = P[i-1] + lcs
            i -= 1
            j -= 1
        elif D[i-1][j] > D[i][j-1]:
            i -= 1
        else:
            j -= 1
    return lcs









def main():
    P = ' kot'
    T = ' pies'
    print(string_compare(P,T))

    P = ' biały autobus'
    T = ' czarny autokar'
    print(string_compare_pd(P,T))

    P = ' thou shalt not'
    T = ' you should not'
    path = string_compare_pd_path(P, T)
    print(path) 

    P = ' ban'
    T = ' mokeyssbanana'
    min_index = string_compare_pd_conect(P,T)
    print(min_index)

    P = ' democrat'
    T = ' republican'
    result = string_compare_pd_longest_subsequence(P, T)
    print(result)

    T = ' 243517698'
    P = ' ' + ''.join(sorted(T[1:]))
    print(string_compare_pd_mono(P, T)) 

main()


