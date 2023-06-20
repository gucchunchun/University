from PIL import Image

def make_colour_barchart(exted_array, total_pixels):
    width = 100
    height = 25

    chart_img = Image.new(mode="RGBA",size=(width, height), color=(0, 0, 0, 0))

    occupied = 0
    for colour in exted_array:
        colour_width = round(colour[1] / total_pixels * 100)
        colour_img = Image.new(mode='RGB', size=(colour_width, height), color=colour[0])
        chart_img.paste(im=colour_img, box=(occupied, 0))
        occupied += colour_width
        if occupied >= 100:
            break

    return chart_img

#pie chart
