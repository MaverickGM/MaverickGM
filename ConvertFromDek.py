def convertFromDek(deckToUse):
    file = open(deckToUse, "r")
    list = []
    for line in file:
        if (line[0:1] == "1"):
            line = line[2:]
            list.append(line)
            #print(line, end='')
    return list

def convertFromDek2(deckToUse):
    file = open(deckToUse, "r")
    list = []
    for line in file:
        #Ensure that up to two characters are checked to be digits. Allows any number of cards from 1 to 99
        cardName = line[2:]
        cardName.strip()
        firstTwoCharacters = line[0:2]
        firstTwoCharacters = firstTwoCharacters.strip()
        if (firstTwoCharacters.isnumeric()):
            if(cardName != 'Swamp\n' and cardName != 'Mountain\n' and cardName != 'Island\n' and cardName != 'Forest\n' and cardName != 'Plains\n' and cardName != ' Swamp\n' and cardName != ' Mountain\n' and cardName != ' Island\n' and cardName != ' Forest\n' and cardName != ' Plains\n'):
                linelist = [firstTwoCharacters,cardName]
                list.append(linelist)
                #print(linelist, end='')
    return list