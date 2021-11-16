# zad 19 unique elements

def unique_elements(arr):
    j = 1
    element = ""
    for i in range (len(arr)):
        if j == len(arr):
            break 
        if arr[i] != arr[j]:
            element = element + str(arr[j]) + ""             
        else:
            element = element + ("")
        if j == (len(arr)-1):
            break 
        j= j + 1
        
    return element

print (unique_elements([2,3,2,5,8,1,9,8]))
        
        
        
            
        
