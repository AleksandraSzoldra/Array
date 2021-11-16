# zad 21
 
 
def big(array):
    big_1 = max(array)
    array.remove(big_1)
    big_2 = max(array)
    return big_2

print(big([5,1,9,6,1]))
    