import os
import urllib.request

def getCardArt(deckToUse):
    modifiedDeckToUse = [card[0] for card in deckToUse]
    outputFolder = os.path.abspath(".") + "\Output\\"
    myNum = 1
    for item in deckToUse:
        noWhiteSpace = item[1].replace(" ","")
        noWhiteSpace = noWhiteSpace.strip()
        try:
            url = "https://api.scryfall.com/cards/named?format=image&version=large&exact=" + noWhiteSpace
            urllib.request.urlretrieve(url,outputFolder+str(myNum)+".jpg")
            myNum += 1
        except:
            print("Card: " + item[1] + " Was not found and will not be included")
            modifiedDeckToUse.pop(myNum-1)
    return modifiedDeckToUse