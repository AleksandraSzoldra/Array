# zad 28

def format(array):
    pion = ""
    poziom = len(array) *5*"_ "
    for i in range (len(array)):
        if array[i]<10:
            pion = pion + "|" + 3*" " + str(array[i]) 
        if array[i]>10 and array[i]<100:
            pion = pion + "|"+ 2* " "+ str(array[i])
        if array[i]>100:
            pion = pion + "|" +" " + str(array[i])
            
    return pion
    
array = [1,23,5]
poziom = len(array) *3*"_ "
print(poziom)
print(format(array)+ "|")
print(poziom)