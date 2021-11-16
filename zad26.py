# zad 26
def separator(array):
    even = ""
    odd = ""
    result = ""
    for i in range (len(array)):
        if array[i]%2==0:
            even = even + str(array[i]) + " "
        else:
            odd = odd + str(array[i]) + " " 
            
    result = even + odd
    return result
    
print(separator([1,2,3,4,5,6]))