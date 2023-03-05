# python3

import sys
import threading
import os


def compute_height(a,vecaki):
    # Write this function
    # Your code here
    berni = []
    for i in range(a):
        berni.append([])
    r = None
    augst = [0] * a

    for i in range(a):
        if vecaki[i] == -1:
            r = 1
        else:
            berni[vecaki[i]].append(i)
    s = [(r,1)]
    max_height = 0

    while s:
        n, m = s.pop()
        augst[n] = m
        max_height = max(max_height, m)
        s.extend([(ch, m+1) for ch in berni[n]])
    return max_height


def main():
    options = {
        "I": ievade_no_tastaturas,
        "F": ievade_no_faila
    }
    text = input("Ievadiet 'I' vai 'F' ")

    # implement input form keyboard and from files
    
    try:
        a, vecaki = options[text]()
    except KeyError:
        print("Nepareiza ievade")
        return
    print(compute_height(a,vecaki))
    # let user input file name to use, don't allow file names with letter a
def ievade_no_faila():
        faila_nosaukums = input("Ievadiet faila nosaukumu: ")

        if "a" in faila_nosaukums:
            print("Nederīgs faila nosaukums")
            return
        try:
            fp = "." + os.sep + "name" + os.sep + faila_nosaukums
            with open(fp, "r") as q:
                a = int(q.readlines())
                vecaki = list(map(int, q.readlines().strip().split()))
            return a, vecaki
        except FileNotFoundError:
            print("Fails netika atrasts")


def ievade_no_tastaturas():
    a = int(input("Ievadiet koka mezglu skaitu: "))
    vec = input()
    vecaki = [int(v) for v in vec.split()]
    return a, vecaki


    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    
if __name__ == "__main__":
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))