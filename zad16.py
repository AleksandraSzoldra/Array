# zad 16
def star(n): #n - tablica 
    star = ""
    for i in range (len(n)):
        quantity = n[i] 
        star = star + quantity * "*" + " " 
    return star

print(star([12,6,4,9,3]))
        
        