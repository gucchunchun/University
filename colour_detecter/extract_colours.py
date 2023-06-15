import extcolors

def exact_color(input_image):
    setting_tolerance = 20
    setting_limit = 11
    colours_x = extcolors.extract_from_path(input_image, tolerance=setting_tolerance, limit=setting_limit)
    # = ([((r.g.b),occurrence),(r.g.b),occurrence)])

    
    white = {"exist": False, "occurrence": 0}
    black = {"exist": False, "occurrence": 0}
    chromatic_pixels = 0
    chromatic_array = []

    #Omit white & black
    for colour in colours_x[0]:
        if colour[0] == (255,255,255):
            white["exist"] = True
            white["occurrence"] = colour[1]
        elif colour[0] == (0,0,0):
            black["exist"] = True
            black["occurrence"] = colour[1]
        else:
            chromatic_array.append(colour)
            chromatic_pixels += int(colour[1])
    
    total_pixels = chromatic_pixels + white["occurrence"] + black["occurrence"]

    return {"colour_array": chromatic_array, "chromatic_pixels": chromatic_pixels, "total_pixels": total_pixels, "white": white, "black": black}


