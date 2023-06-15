from extract_colours import exact_color
from make_colour_chart import make_colour_barchart

exact_color("tester.png")
img = make_colour_barchart(exact_color("tester.png")["colour_array"],exact_color("tester.png")["chromatic_pixels"])

img.save("/Users/yuna/Documents/GitHub/University/colour_detecter/tester_1.png")