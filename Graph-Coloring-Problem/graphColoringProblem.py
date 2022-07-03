dictOfAdjacency = dict()
verticesAndColors = dict()

with open('test1.txt') as file:
    linesExceptFirst = file.readlines()[1:]   # All lines except first line

    for lines in linesExceptFirst:
        theLine = lines.strip()
        splittedTheLine = theLine.split(" ")

        if int(splittedTheLine[1]) in dictOfAdjacency:
            dictOfAdjacency[int(splittedTheLine[1])].append(int(splittedTheLine[2]))
        else:
            dictOfAdjacency[int(splittedTheLine[1])] = [int(splittedTheLine[2])]
            verticesAndColors[int(splittedTheLine[1])] = -1  # Make default color value of vertices -1 to think them as uncolored

        if int(splittedTheLine[2]) not in dictOfAdjacency:
            dictOfAdjacency[int(splittedTheLine[2])] = [int(splittedTheLine[1])]
            verticesAndColors[int(splittedTheLine[2])] = -1 # Make default color value of vertices -1 to think them as uncolored
        else:
            dictOfAdjacency[int(splittedTheLine[2])].append(int(splittedTheLine[1]))

    itemsPair = dictOfAdjacency.items()

    for verts, listOfAdj in itemsPair:
        counter = 0
        verticesAndColors[verts] = 0
        while counter < len(listOfAdj):
            for adjsOfCurrentVert in listOfAdj:
                try:
                    if verticesAndColors[verts] == verticesAndColors[adjsOfCurrentVert]:
                        verticesAndColors[verts] += 1
                except:
                    continue
            counter += 1

    lengthList = []
    colorsList = []
    for a in sorted(verticesAndColors.keys()):
        colorsList.append(verticesAndColors[a])
        if verticesAndColors[a] not in lengthList:
            lengthList.append(verticesAndColors[a])

    firstLine = len(lengthList)
    strFirstLine = str(firstLine)

    nextLine = "\n"

    with open('output.txt', 'w') as f:
        f.write(strFirstLine)
        f.write(nextLine)
        for i in colorsList:
            f.write(str(i)+" ")