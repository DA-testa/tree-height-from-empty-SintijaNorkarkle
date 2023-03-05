# python3
"""
Sintija Norkārkle, RDCPO, 1. grupa
"""
import sys
import threading
import numpy as np

def compute_height(nnn, parents):
    """
    šī funkcija aprēķina koka augstumu.
    divi argumenti:
        - nnn: mezglu skaits kokā
        - parents: veselu skaitļu masīvs, kas attēlo katra mezgla vecāku
    tiek iegūts koka augstums
    """
    # izveido masīvu, lai glabātu katra mezgla augstumu
    heights = np.zeros(nnn, dtype=int)
    # notiek iterācija caur visiem mezgliem
    for i in range(nnn):
    # ja pašreizējā mezgla augstums ir 0, tas nozīmē, ka nav vēl aprēķināts tā augstums
        if heights[i] == 0:
    # sākot ar pašreizējo mezglu, notiek virzība uz augšu līdz saknei
            height = 0
            j = i
        while j != -1:
    # ja jau ir aprēķināts šī mezgla augstums, pievieno to pašreizējam augstumam
            if heights[j] != 0:
                height += heights[j]
                break
    # pretējā gadījumā palielina augstumu un pārvietojas uz vecāku
            height += 1
            j = parents[j]
    # tagad, kad ir sasniegta sakne, notiek kustība uz leju pa visiem mezgliem un tiek saglabāts to augstums
        j = i
        while j != -1:
            if heights[j] != 0:
                height += heights[j]
                break
            heights[j] = height
            height -=1
            j = parents[j]
    # atgriež visu mezglu maksimālo augstumu
    return np.max(heights)

def main():
    """
    šajā funkcijā tiek nolasīti dati vai nu no faila, vai nu no tastatūras
    tiek izsaukta compute_height funkcija un izvadīts rezultāts
    """
    text = input("Ievadiet 'I' vai 'F': ").strip()
    # ievada vērtības no tastatūras
    if "I" in text:
        aaa = int(input("Ievadiet skaitu: ").strip())
        vecaki = np.array(list(map(int,input("Ievadiet masīvu: ").split())))
    # ievada vērtības no faila
    elif "F" in text:
    # nolasa faila nosaukumu
        faila_nosaukums = input()
    # pārbauda vai faila nosaukums satur "a"
        if "a" in faila_nosaukums:
            print("Nederīgs faila nosaukums!")

        try:
    # atver failu un nolasa vērtības
            faila_nosaukums = "test/" + faila_nosaukums
            with open(faila_nosaukums, 'r' ,  encoding="utf8") as file:
                aaa = int(file.readline().strip())
                vecaki = np.array(list(map(int, file.readline().split())))

        except FileNotFoundError:
    # ja fails neeskistē, izvada paziņojumu
            print("Fails netika atrasts!")
            return

    height = compute_height(aaa,vecaki)
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
if __name__ == "__main__":

    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
