def unique(arr):
    element = "" 
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[i] != arr[j]:
                element = element + str(arr[j]) + ""             
            else:
                element = element + ("")
    return element

print(unique([2,2,3,2]))
            

            