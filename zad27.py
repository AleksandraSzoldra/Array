# zad 27

def string(array):
    new = "" 
    for i in range (len(array)):
        new = new + str(array[i])
        if i<(len(array)-1):
            new = new + ","
        
        
    return new

print(string([5,4,3,2,6,5]))
        