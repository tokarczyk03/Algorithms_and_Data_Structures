#nieskonczone
import time

def naiwna_v2(S, W):
    m = 0
    i = 0
    calls = 0
    count = 0
    while m < len(S) - len(W) + 1:
            if S[m + i] == W[i]:
                calls += 1
                if i == len(W) - 1:
                    count += 1
                    m += 1
                    i = 0
                else:
                    i += 1
            else:
                calls += 1
                m += 1
                i = 0
    return count, calls


def rabin_karp(S, W):
    d = 256
    q = 101
    hW = hash(W)
    hS = 0
    h = 1
    count = 0
    calls = 0
    collisions = 0

    for i in range(len(W)-1):
        h = (h*d) % q

    for m in range(len(S)-len(W)+1):
        if m == 0:
            hS = hash(S[m:m+len(W)])
        else:
            hS = (d * (hS - ord(S[m-1]) * h) + ord(S[m+len(W)-1])) % q
            if hS < 0:
                hS += q

        calls += 1
        if hS == hW:
            if S[m:m+len(W)] == W:
                count += 1
            else:
                collisions += 1

    return count, calls, collisions

def hash(word):
    hw = 0
    d = 256 
    q = 101  
    for i in range(len(word)):  
        hw = (hw*d + ord(word[i])) % q  
    return hw


def main():

    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()
    S = ' '.join(text).lower()

    ##############################
    t_start = time.perf_counter()

    wyst, calls = naiwna_v2(S,'time.')
    print(f'{wyst}; {calls}')

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


    ##############################
    t_start = time.perf_counter()

    wyst, calls, collisions = rabin_karp(S,'time.')
    print(f'{wyst}; {calls}; {collisions}')

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
main()