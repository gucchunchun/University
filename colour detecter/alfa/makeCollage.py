from PIL import Image
import glob

folder="/Users/yuna/Documents/GE/samplesUni/all"
images = glob.glob(folder + "/pickedColour*")
imageNum = len(images)

collageWidth = Image.open(images[0]).width
Height = Image.open(images[0]).height
collageHeight = Height * imageNum

collage = Image.new("RGB",(collageWidth,collageHeight))

for i, image in enumerate(images):
    copyImage = Image.open(image)
    collage.paste(copyImage, (0,Height * i))

collage.save(folder + "/colours.png")

# .png
folder="/Users/yuna/Documents/GE/GEsample/UK/mainColor"
images = glob.glob(folder + "/*.png")
imageNum = len(images)

collageWidth = Image.open(images[0]).width
Height = Image.open(images[0]).height
collageHeight = Height * imageNum

collage = Image.new("RGB",(collageWidth,collageHeight))

for i, image in enumerate(images):
    copyImage = Image.open(image)
    collage.paste(copyImage, (0,Height * i))

collage.save(folder + "/colours.png")