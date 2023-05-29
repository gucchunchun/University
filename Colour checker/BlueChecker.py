import cv2
import numpy as np​
import glob
import os 


def mainColour(sample):
    img = cv2.imread(sample)
    # changing Colour space to HSV from RGB 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # The 12 major colors of the color wheel
    # 下限はhttps://www.e-paint.co.uk/BS381-colour-chart.aspにおいて青となの付くものだけ
    mask_blue = cv2.inRange(img, (159, 1, 25), (255, 100, 100))
    hasBlue = np.sum(mask_blue)
    if hasBlue > 0:
        return 1
    else:
        return 0


counter = 0
folder = ''
samples=glob.glob(folder + '/pickedColour*.jpg')
for i, sample in enumerate(samples):
    counter += mainColour(sample)

print("Samples: " + len(samples)-1)
print("Including Blue: " +counter)
print("Ratio: " + counter/(len(samples)-1))
    