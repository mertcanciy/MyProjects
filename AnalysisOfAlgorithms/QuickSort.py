import time
import random



list =[random.randint(1,1000) for x in range(1000)]
def QuickSort(liste):
    listleft=[]
    listright=[]
    listresult=[]

    for i in range(1,len(liste)):
        if liste[i]<=liste[0]:
            listleft.append(liste[i])
        else:
            listright.append(liste[i])
    if len(listleft)>0:
        listresult=QuickSort(listleft)
    if len(liste)>0:
        listresult.append(liste[0])
    if len(listright) > 0:
        listresult.extend(QuickSort(listright))
    return listresult
k=int(input("please enter the k value: "))
start_time= time.time()
listresult=QuickSort(list)
if k<len(listresult):
    print(listresult[k-1])
print("--- %s seconds ---" % (time.time() - start_time))
