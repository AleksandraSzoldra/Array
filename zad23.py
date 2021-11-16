# zad 23

def median(array): #bubblesort 
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
        
    if len(array)%2 ==0: #parzysta ilosc elementow
        middle = int(len(array)/2)
        med = (array[middle-1] + array[middle])/2
    else: #nieparzysta ilosc elementow
        middle = int((len(array)/2)-0.5)
        med = array [middle]
             
    return med

print(median([6,8,3,1,0,5,7]))
            
            
            