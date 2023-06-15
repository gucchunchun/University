from PIL import Image
import math

def make_colour_barchart(extcolor_array, pixels):
    width = 100
    height = 25

    chart_img = Image.new(mode="RGB", size=(width, height))

    occupied = 0
    for colour in extcolor_array:
        colour_width = round(colour[1] / pixels * 100)
        colour_img = Image.new(mode='RGB', size=(colour_width, height), color=colour[0])
        chart_img.paste(im=colour_img, box=(occupied, 0))
        occupied += colour_width
        if occupied >= 100:
            break

    return chart_img

#pie chart
