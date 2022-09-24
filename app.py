import easyocr
import argparse
from pathlib import Path 
import os
import glob

parser = argparse.ArgumentParser()
parser.add_argument('--src', type=str,required=True, help="Source Folder Path")
parser.add_argument('--dest', type=str,required=True, help="destination folder path")
args = parser.parse_args()

def appendToFile(data,fileName):
    absolutePath = dest+"/result-"+fileName+".txt"
    if os.path.isfile(absolutePath):
        os.remove(absolutePath)
    f = open(absolutePath,"a")
    for line in data:
        f.write(line+"\n")

def findTextFromImage(fileName):
    
    targetFile = os.path.basename(fileName)
    print("working on filename -> {}".format(targetFile))
    result = reader.readtext(fileName)
    print("Total {} words Found ".format(len(result)))
    data = []
    for x in result:
        data.append(x[1])
    appendToFile(data,targetFile)
    print("OCR Completed For Filename -> {}".format(os.path.basename(targetFile)))
    

reader = easyocr.Reader(['en','hi'],gpu=True) # this needs to run only once to load the model into memory
src = args.src
dest = args.dest


listOfImages = glob.glob(src+"/*")

for image in listOfImages:
    findTextFromImage(image)
