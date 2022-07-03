import time
import random

list =[random.randint(1,10000) for x in range(10000)]
def SelectedWithTree(k,liste):
    while True:
        listleft=[]
        listright=[]
        first=liste[0]
        last=liste[len(liste)-1]
        middle=liste[(int((len(liste))/2)-1)]
        pivot=int((first+middle+last)/3)

        for i in range(0,len(liste)):
            if liste[i]<=pivot:
                listleft.append(liste[i])
            else:
                listright.append(liste[i])

        if len(liste)==1:
            break
        if k<len(listleft) and len(listleft)>0:
            if len(listleft)==len(liste):
                break
            liste=listleft



        elif k>=len(listleft) and len(listright)>0 :
            k=k-len(listleft)
            liste=listright



    return liste[0]
k=int(input("please enter the k value: "))
start_time= time.time()
result=SelectedWithTree(k-1,list)
print(result)
print("--- %s seconds ---" % (time.time() - start_time))

