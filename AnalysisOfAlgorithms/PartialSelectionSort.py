import time
import random

list =[random.randint(1,100) for x in range(10000)]

def SetN():
    n = input("n: ")

    if n.isnumeric():
        return int(n)
    else:
        print("Invalid Input")
        SetN()

def SelectionSort(array, n):
    smallest = 0
    check = False
    for i in range(len(array)):
        for j in range(i, len(array)):
            if not check:
                if array[j] < array[i]:
                    smallest = j
                    check = True
            else:
                if int(array[j]) < array[smallest]:
                    smallest = j
        if smallest != 0:
            x1 = array[i]
            array[i] = array[smallest]
            array[smallest] = x1
            smallest = 0
            check = False

    if n > len(array):
        return array[-1]
    elif n < 0:
        return array[0]
    else:
        return array[n]

n = SetN()
start_time = time.time()
print("n(th) element: ", SelectionSort(list, n))
print("--- %s seconds ---" % ((time.time() - start_time)))