def list_sort(lista):
    evens_list = []
    for x in lista:
        if type(x) is int:
            if x % 2 == 0:
                evens_list.append(x)
    evens_list.sort()
    
    odd_list = []
    for y in lista:
        if type(y) is int:
            if y % 2 == 1:
                odd_list.append(y)
    odd_list.sort()

    char_list = []
    for y in lista:
        if str(y).isalpha():
            char_list.append(y)
    char_list.sort()

    lis = {}
    lis['evens'] = evens_list
    lis['odd'] = odd_list
    lis['chars'] = char_list
    print (lis)   

list_sort(["a",1,2,4,"b",5.1])
    

