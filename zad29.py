# zad 29
def subset(array, tab):
    g = 0
    f = 0 
    for i in range(len(array)):
        if array[i] in tab:
            g +=1
        else:
            f+=1
    if g !=0:
        return True
    else:
        return False 
    
print(subset([4,5,6],[4,5,6,1,2,3]))