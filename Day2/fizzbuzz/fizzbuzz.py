# def fizzbuzz(a,b):


lista, listb = [3,4,7,4,6,8,0,2], [3,5,6,7,5,6,0]

x = len(lista) + len(listb)

def fizzbuzz(x):
        if x % 3 == 0 and x % 5 == 0:
                print("FizzBuzz")
                return

        if x % 3 == 0:
                print("Fizz")
                return

        if x % 5 == 0:
                print("Buzz")
                return

        else:
                # print(x)
                print("length: ", x)
                return

fizzbuzz(x)

