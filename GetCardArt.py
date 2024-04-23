import os
import urllib.request

def getCardArt(deckToUse):
    outputFolder = os.path.abspath(".") + "\Output\\"
    myNum = 0
    for item in deckToUse:
        myNum += 1
        noWhiteSpace = item.replace(" ","")
        noWhiteSpace = noWhiteSpace.strip()
        url = "https://api.scryfall.com/cards/named?format=image&version=large&exact=" + noWhiteSpace
        urllib.request.urlretrieve(url,outputFolder+str(myNum)+".jpg")