import time
import random

list =[random.randint(1,10000) for x in range(10000)]

def bestCaseForHeap():
    returnedList = [100]*10000
    return returnedList

def worstCaseForHeap():
    list = [random.randint(1, 5000) for x in range(5000)]
    list.sort()
    return list

def HeapSort(k,liste,liste2):
    while True:
        x=-1
        us=1
        y=0
        for i in range(len(liste)):
            if i>y:
                x=y
                y+=2**us
                us+=1

            for j in range(2):
                try:

                    if liste[i]<liste[y+((i-x-1)*2)+j+1]:

                        sayi=liste[i]
                        liste[i]=liste[y+((i-x-1)*2)+j+1]
                        liste[y + ((i - x - 1) * 2) + j + 1]=sayi
                        childnum=i
                        if i%2==1:
                            parentnum=(i-1)/2
                        else:
                            parentnum = (i - 2) / 2


                        while liste[parentnum]<liste[childnum]:
                            sayi = liste[parentnum]
                            liste[parentnum] = liste[childnum]
                            liste[childnum] = sayi
                except:
                    continue



        num=len(liste)-1
        liste2.append(liste[0])
        liste[0]=liste[num]
        liste.pop(num)

        if len(liste)==0 :
            break
    return liste2[len(liste2)-k]


liste2=[]
k=int(input("please enter the k value: "))
start_time= time.time()
result=HeapSort(k,worstCaseForHeap(),liste2)
print(result)
print("--- %s seconds ---" % (time.time() - start_time))