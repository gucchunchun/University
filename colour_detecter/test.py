import pickle
import numpy as np

class colours_list():
    def __init__(self, industry, sub):
        self.industry = industry
        self.sub_category = sub
        self.array = []
        self.pixel = 0

    def add_colours(self, colour_array):
        for colour in colour_array:
            colour_rgb = colour[0]
            colour_occurrences = colour[1]
            self.pixel += colour_occurrences
            
            colour_in_list = False
            for arr_colour in self.array:
                if arr_colour[0] == colour_rgb:
                    arr_colour[1] += colour_occurrences
                    colour_in_list = True
                    break
            if colour_in_list == False:
                self.array.append(colour)
    
    def make_record(self, txt_path):
        f= open(txt_path, "a")
        f.truncate(0) #byte数
        f.write(f"Industry: {self.industry}\nSabcategory: {self.sub_category}\n")
        for colour in self.array:
            f.write(f"{colour[2]}: {colour[1]/self.pixel * 100}% ({colour[1]})\n")
        f.write("\n\n\n")

def save_object(obj, save_name):
    try:
        with open(save_name + ".pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

array = [[(0,0,0), 100, "black"], [(0,0,0), 100, "black"], [(255, 255, 255), 100, "white"],[(255, 0, 0), 100, "red"]]

test_list = colours_list("taniguchi", "yuna")
test_list.add_colours(array)

save_object(test_list)

test2 = load_object("test.pickle")
print(test2.array)