import time
import random

list =[random.randint(1,10000) for x in range(10000)]
def SelectedWithFirst(k,liste):
    listleft=[]
    listright=[]


    for i in range(1,len(liste)):
        if liste[i]<=liste[0]:
            listleft.append(liste[i])
        else:
            listright.append(liste[i])
    result=0
    if k<len(listleft):
        result=SelectedWithFirst(k,listleft)
    if k==len(listleft):
        result=liste[0]
    if k>len(listleft):
        result=SelectedWithFirst(k-len(listleft)-1,listright)
    return result
k=int(input("please enter the k value: "))
start_time= time.time()
result=SelectedWithFirst(k-1,list)
print(result)
print("--- %s seconds ---" % (time.time() - start_time))