# python3
"""
Sintija Norkārkle
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
    heights = [0] * aaa
    for i in range(aaa):
        if heights[i] != 0:
            continue
        height = 0
        j = i
        while j != -1:
            if heights[j] != 0:
                neight += heights[j]
                break
            height += 1
            j = vecaki[j]
        j = i
        while j != -1:
            if heights [j] != 0:
                height += heights[j]
                break
            heights [j] = height
            height -=1
            j = vecaki[j]

    return max(heights)

def main():
    """
    xdbf
    """
    text = input("Ievadiet 'I' vai 'F' ").strip()
    # implement input form keyboard and from files
    if "I" in text:
        aaa = int(input("Ievadiet skaitu: ").strip())
        vecaki = list(map(int,input("Ievadiet virkni: ").split()))
    elif "F" in text:

        faila_nosaukums = input("Ievadiet faila nosaukumu: ").strip()
        faila_atr = "." + os.sep + "name" + os.sep + faila_nosaukums
        if "a" in faila_nosaukums:
            print("Nederīgs faila nosaukums")

        try:

            with open(faila_atr, mode = "r" ,  encoding="utf8") as file:
                aaa = int(file.readline().strip())
                vecaki = list(map(int, file.readline().split()))

        except FileNotFoundError:
            print("Fails netika atrasts")
            return
    else:
        print("Error")
        return
    height = compute_height(aaa,vecaki)
    print(height)


    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
if __name__ == "__main__":

    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
