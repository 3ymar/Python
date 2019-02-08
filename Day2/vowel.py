x = input(str("User:"))
from collections import Counter  #used to import the count in a programm

def function(y):
    inlist=[]
    vowels=["a","e","i","o",]
    for char in y:
        if char in vowels:
            inlist.append(char)
            inlist.sort()        
            output = Counter(inlist) 

    print(output)
function(x)

