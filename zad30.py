# zad 30

import random
def rand_element(array): #array- ilosc elementow w tablicy tab
    tab = []
    for i in range (array):
        g = random.random()
        tab = tab + [g]
    return tab

print(rand_element(3))