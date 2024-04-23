import ConvertFromDek
import GetCardArt
import DeleteOutputFolder
import os
import aspose.words as aw

deckToUse = []

currentLocation = os.path.abspath(".") + "\Input\\"
for root, dir, files in os.walk(currentLocation):
    for file in files:
        inputFolder = currentLocation + files[0]
        deckToUse = ConvertFromDek.convertFromDek(inputFolder)

GetCardArt.getCardArt(deckToUse)

imageDoc = aw.Document()
imageDocBuilder = aw.DocumentBuilder(imageDoc)
imageDocBuilder.page_setup.left_margin = 0
imageDocBuilder.page_setup.right_margin = 0
imageDocBuilder.page_setup.top_margin = 0
imageDocBuilder.page_setup.bottom_margin = 0
outputFolder = os.path.abspath(".") + "\Output\\"

for i in range(len(deckToUse)):
    imageDocBuilder.insert_image(outputFolder+str(i+1)+".jpg",175,247)

DeleteOutputFolder.deleteOutputFolder()

fileName = os.path.abspath(".")+"\Output\\OutputPictures.pdf"
imageDoc.save(fileName)