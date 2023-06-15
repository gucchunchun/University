#colour check & counter

import cv2
import numpy as np
import glob


def hasColour(sample):
    global redCounter
    global redCounter
    global orangeCounter
    global yellowCounter
    global greenCounter
    global cyanCounter
    global blueCounter
    global purpleCounter 

    global allRed
    global allOrange
    global allYellow
    global allGreen
    global allCyan
    global allBlue
    global allPurple


    img = cv2.imread(sample)
    # changing Colour space to HSV from RGB 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #https://www.adeept.com/learn/tutorial-169.html
    mask_red1 = cv2.inRange(img,(0, 43, 46), (10, 225, 225) )
    mask_red2 = cv2.inRange(img,(156, 43, 46), (180, 225, 225) )

    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    mask_orange = cv2.inRange(img,(11, 43, 46), (25, 225, 225) )
    mask_yellow = cv2.inRange(img,(26, 43, 46), (34, 225, 225) )
    mask_green = cv2.inRange(img,(35, 43, 46), (77, 225, 225) )
    mask_cyan = cv2.inRange(img, (78, 43, 46), (99, 225, 225))
    mask_blue = cv2.inRange(img, (100, 43, 46), (124, 225, 225))
    mask_purple = cv2.inRange(img, (125, 43, 46), (155, 225, 225))


    masked ={"red": mask_red, "orange":mask_orange, "yellow":mask_yellow, "green":mask_green,"cyan":mask_cyan, "blue":mask_blue, "violet":mask_purple}

    # .items() id for make the dictionary as a tuple
    for colour, mask in masked.items():
        has = np.sum(mask)
        if (has>0):
            if colour == "red":
                redCounter+=1
                allRed +=1
            elif colour == "orange":
                orangeCounter += 1
                allOrange +=1
            elif colour == "yellow":
                yellowCounter += 1
                allYellow +=1
            elif colour == "green":
                greenCounter += 1
                allGreen +=1
            elif colour == "cyan":
                cyanCounter += 1
                allCyan +=1
            elif colour == "blue":
                blueCounter += 1
                allBlue +=1
            else:
                purpleCounter += 1
                allPurple +=1
        continue
        

allSamples = 0
allRed = 0
allOrange = 0
allYellow = 0
allGreen = 0
allCyan = 0
allBlue = 0
allPurple = 0

folder1 ="/Users/yuna/Documents/GE/GEsample/UK/"
folders=glob.glob(folder1 + '*C')


for folder in folders:
    foldername = folder.replace(folder1,"")
    samples=glob.glob(folder + '/pickedColour*.jpg')

    redCounter = 0
    orangeCounter = 0
    yellowCounter = 0
    greenCounter = 0
    cyanCounter = 0
    blueCounter = 0
    purpleCounter = 0

    for i, sample in enumerate(samples):
        hasColour(sample)

    colourCounter ={"red": redCounter, "orange":orangeCounter, "yellow":yellowCounter, "green":greenCounter, "cyan":cyanCounter, "blue":blueCounter, "purple": purpleCounter}
    NumOfSample = len(samples)
    allSamples += NumOfSample
    f= open("/Users/yuna/Documents/GE/GEsample/UK/result.txt", "a")
    f.write(foldername+ "   Samples: "+str(NumOfSample)+ "\n")
    
    for colour, counter in colourCounter.items():

        f.write(colour + ": "+ str(counter/NumOfSample) +"(" +str(counter)+")\n")
    f.write("\n\n\n")

allColourCounter = {"red": allRed, "orange":allOrange, "yellow":allYellow, "green":allGreen, "cyan":allCyan, "blue":allBlue, "purple": allPurple}
f.write("All samples: "+str(allSamples)+ "\n")
for colour, counter in allColourCounter.items():
    f.write(colour + ": "+ str(counter/allSamples) + "\n")
f.write("Cyan+blue: "+ str((allCyan + allBlue)/allSamples) + "\n")
    