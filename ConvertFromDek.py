def convertFromDek(deckToUse):
    file = open(deckToUse, "r")
    list = []
    for line in file:
        if (line[0:1] == "1"):
            line = line[2:]
            list.append(line)
            #print(line, end='')
    return list