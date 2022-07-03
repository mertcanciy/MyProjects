import time
import random

def bestCaseGenerate():
    list = [random.randint(1, 10000) for x in range(10000)]
    list.sort()
    return list


def MergeSort(liste):
    listleft=[]
    listright=[]
    listresult=[]
    #print(liste)
    if len(liste) != 1:
        for i in range(0,len(liste)):
            if i<(len(liste)/2):
                listleft.append(liste[i])
            else:
                listright.append(liste[i])
        i=0
        j=0
        listleft=MergeSort(listleft)
        listright=MergeSort(listright)

        while i<len((listleft)) or j<len((listright)):
            if i >= len(listleft):
                listresult.append((listright)[j])
                j+=1
                continue
            elif j>=len(listright):
                listresult.append((listleft)[i])
                i+=1
                continue

            if listleft[i]<listright[j]:
                listresult.append((listleft)[i])
                i+=1
            else:
                listresult.append((listright)[j])
                j+=1

    else:
        listresult.append(liste[0])
    return listresult


k=int(input("please enter the k value: "))
start_time= time.time()
listresult=MergeSort(bestCaseGenerate())
if k<len(listresult):
    print(listresult[k-1])
print("--- %s seconds ---" % (time.time() - start_time))