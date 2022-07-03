import random
import time
mainArray = []

def bestCaseListGenerate():
    list =[random.randint(1, 1000) for x in range(10000)]
    list.sort()
    return list

def worstCaseListGenerate():
    list = [random.randint(1, 1000) for x in range(10000)]
    list.sort(reverse=True)
    return list

def SetN():
    n = input("n: ")

    if n.isnumeric():
        return int(n)
    else:
        print("Invalid Input")
        SetN()


def InsertionSort(array, n):

    for i in range(len(array)):
        index = i
        for j in range(i, -1, -1):
            if array[index] < array[j]:
                x1 = array[index]
                array[index] = array[j]
                array[j] = x1
                index -= 1

    if n > len(array):
        return array[-1]
    elif n < 0:
        return array[0]
    else:
        return array[n]


n = SetN()
start_time = time.time()
print("n(th) element: ", InsertionSort(worstCaseListGenerate(), n))
print("--- %s seconds ---" % ((time.time() - start_time)))