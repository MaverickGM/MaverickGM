import os
import glob

def deleteOutputFolder():
    outputFolder = os.path.abspath(".") + "\Output\\"
    filesInOutput = glob.glob(outputFolder+'*')
    for file in filesInOutput:
        #print(file)
        os.remove(file)