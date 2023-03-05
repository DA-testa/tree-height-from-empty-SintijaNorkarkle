# python3
"""
programma ...
"""
import sys
import threading
import os

def compute_height(aaa, vecaki):
    """
    xcvn
    """
    # Write this function
    # Your code here
    berni = []
    for i in range(aaa):
        berni.append([])
    rrr = None
    augst = [0] * aaa

    for i in range(aaa):
        if vecaki[i] == -1:
            rrr = i
        else:
            berni[vecaki[i]].append(i)
    sss = [(rrr,1)]
    max_height = 0

    while sss:
        nnn, mmm = sss.pop()
        augst[nnn] = mmm
        max_height = max(max_height, mmm)
        sss.extend([(ch, mmm+1) for ch in berni[nnn]])
    return max_height

def main():
    """
    xdbf
    """
    text = input("Ievadiet 'I' vai 'F' ")
    # implement input form keyboard and from files
    if "F" in text:

        faila_nosaukums = input("Ievadiet faila nosaukumu: ")

        if "a" in faila_nosaukums:
            print("Nederīgs faila nosaukums")
            return
        try:
            faila_atr = "." + os.sep + "name" + os.sep + faila_nosaukums
            with open(faila_atr, mode = "r" ,  encoding="utf8") as file:
                aaa = int(file.readline())
                vecaki = list(map(int, file.readline().strip().split()))
            return aaa, vecaki
        except FileNotFoundError:
            print("Fails netika atrasts")
    if "I" in text:
        aaa = int(input("Ievadiet koka mezglu skaitu: "))
        vec = input()
        vecaki = [int(v) for v in vec.split()]
        return aaa, vecaki

    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
if __name__ == "__main__":
    main()
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
