# zad13 Array

def power(tab):
    m = ""
    for i in tab:
        m = m + " "+ str(i**2)
        
    return m 
    
print(power([8,2,5,1]))