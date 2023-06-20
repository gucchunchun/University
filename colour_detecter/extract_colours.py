import extcolors
import json
import colour_converter as cc
from make_colour_chart import make_colour_barchart
from colour_distant import colour_distant
from enum import Enum
import glob, os
import pickle



class countries(Enum):
        uk = 0
        jp = 1

class colour_info():
    def __init__(self, chromatic_array, white_occurrences, black_occurrences, chromatic_pixels):
        self.array = chromatic_array
        self.white = white_occurrences
        self.black = black_occurrences
        self.pixel = chromatic_pixels
        
    def traditional_clour_array(self, country):
        colour_data_file = open("data_set/" + country + ".json")
        colour_data = json.loads(colour_data_file.read())

        new_tuple_array = []

        for tuple in self.array:
            likey_color = ()
            minimum_distant = 10000.0
            rgb = tuple[0]

            for i in range(0, len(colour_data)):
                data_rgb = cc.hex_to_rgb(colour_data[i]["hex"])
                distant = colour_distant(rgb, data_rgb).ciede2000
                if distant <= minimum_distant:
                   minimum_distant = distant
                   #make a tuple = ((rgb), occarance, clolour_name)
                   #tupleはimmutableだけどメモリ効率が高い
                   likey_color = [data_rgb, tuple[1], colour_data[i]["color"]]
                   if minimum_distant == 0:
                      break
            new_tuple_array.append(likey_color)
        return new_tuple_array

def ext_color(input_image):
    setting_tolerance = 20
    setting_limit = 11
    tuples_x = extcolors.extract_from_path(input_image, tolerance=setting_tolerance, limit=setting_limit)
    # = ([((r.g.b),occurrence),(r.g.b),occurrence)])

    
    white = 0
    black = 0
    chromatic_pixels = 0
    chromatic_array = []

    #Omit white & black
    for tuple in tuples_x[0]:
        if tuple[0] == (255,255,255):
            white = tuple[1]
        elif tuple[0] == (0,0,0):
            black = tuple[1]
        else:
            chromatic_array.append(list(tuple))
            chromatic_pixels += tuple[1]
    
    return colour_info(chromatic_array, white, black,chromatic_pixels)

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
    def delete_colours(self, colour_tuple):
        self.array.remove(colour_tuple)
        self.pixel -= colour_tuple[1]
    
    def make_record(self, save_path):
        f= open(save_path + ".txt", "a")
        f.truncate(0) #byte数
        f.write(f"Industry: {self.industry}\nSabcategory: {self.sub_category}\n")
        for colour in self.array:
            f.write(f"{colour[2]}: {colour[1]/self.pixel * 100}% ({colour[1]})\n")
        f.write("\n\n\n")

def get_pixcel(elm):
    return elm[1]  

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

def ext_record_color(folder, list:colours_list, country : countries):
    folder_name = folder if folder.endswith("/") else folder + "/" 
    print(folder_name)
    files = glob.glob(folder_name + "*")
    second_loop = []
    colour_bar_ids = []

    number_of_files = len(files)
    counter = 1
    has_done = False

    for file in files:
        print(f"    {counter}/{number_of_files}ファイル目")
        file_name = file[file.rfind("/")+1:]
        if not file.endswith(".png"):
            if file.endswith(".pickle"):
                list.array = load_object(file).array
                list.pixel = load_object(file).pixel
                has_done = True
                break
            counter +=1
            continue
        elif file.endswith("_colour.png"):
            if file.endswith("_" + country.name + "_colour.png"):
                file_id = file_name.replace("_" + country.name + "_colour.png","")
                colour_bar_ids.append(file_id)
            counter +=1
            continue
        elif file.endswith("_sample.png"):
            second_loop.append(file)
            counter +=1
            continue
        # file_name = ~~~/~~~/~~~/scrennshot-{company_name}-{time}.png
        index1 = file_name.find("-")
        index2 = file_name.find("-", index1 + 1)
        file_id = file_name[index1 + 1: index2]

        #一つ一つのデータごとlistに入れればよかった？
        file_colour_info = ext_color(file)
        file_traditional_colour_array = file_colour_info.traditional_clour_array(country.name)
        img = make_colour_barchart(file_traditional_colour_array,file_colour_info.pixel)
        img.save(folder_name + file_id +  "_" + country.name + "_colour.png")
        os.rename(file, folder_name + file_id + "_sample.png")
        list.add_colours(file_traditional_colour_array)
        counter +=1

    if has_done == False:
        print("    重複チェック中")
        for sample in second_loop:
            has_colour_chart = False
            sample_name = sample[sample.rfind("/")+1:]
            sample_id = sample_name.replace("_sample.png", "")
            for id in colour_bar_ids:
                if sample_id != id:
                    continue
                else:
                    colour_bar_ids.remove(id)
                    has_colour_chart = True
                    break
            print("    extracting colour")
            file_colour_info = ext_color(sample)
            file_traditional_colour_array = file_colour_info.traditional_clour_array(country.name)
            list.add_colours(file_traditional_colour_array)
            if has_colour_chart == False:
                img = make_colour_barchart(file_traditional_colour_array,file_colour_info.pixel)
                img.save(folder_name + file_id +  "_" + country.name + "_colour.png")

        save_path = folder_name + country.name + "_" + list.industry +  "_" + list.sub_category
        list.array.sort(key=get_pixcel, reverse=True)
        list.make_record(save_path + ".txt")
        img = make_colour_barchart(list.array, list.pixel)
        img.save(save_path + "_colour.png")
        save_object(list, save_path)
    print(folder_name + "is DONE")


def uk_colour_ext():
    sample_folder="/Users/yuna/Documents/GE/samples/"
    folders = glob.glob(sample_folder + "*")
    uk_colour_list = colours_list("United Kingdom","")

    number_of_folder= len(folders)+ 1
    counter = 1

    for folder in folders:
        print(f"\n{counter}/{number_of_folder}ファイル目:")
        if folder.endswith("_colour.png") or folder.endswith(".txt") or folder.endswith(".pickle"):
            continue
        industry = folder.replace(sample_folder,"")
        if industry =="public":
            folder_colour_list = colours_list(industry,"")
            public_subfolders = glob.glob(folder + "/*")
            for sub_folder in public_subfolders:
                if sub_folder.endswith("_colour.png") or sub_folder.endswith(".txt") or sub_folder.endswith(".pickle"):
                    continue
                sub_category = sub_folder.replace(folder + "/", "")
                subfolder_colour_list = colours_list(industry, sub_category)
                ext_record_color(sub_folder,subfolder_colour_list, countries.uk)
                folder_colour_list.add_colours(subfolder_colour_list.array)
            save_path = folder + "/uk_public"
            folder_colour_list.array.sort(key=get_pixcel, reverse=True)
            print(folder_colour_list.array)
            folder_colour_list.make_record(save_path + ".txt")
            img = make_colour_barchart(folder_colour_list.array, folder_colour_list.pixel)
            img.save(save_path + "_colour.png")
            save_object(folder_colour_list, save_path)
        else:
            sub_category = ""
            folder_colour_list = colours_list(industry,sub_category)
            ext_record_color(folder,folder_colour_list, countries.uk)
        uk_colour_list.add_colours(folder_colour_list.array)
        counter +=1
    save_path = sample_folder + "Unitedkingdom"
    uk_colour_list.array.sort(key=get_pixcel, reverse=True)
    uk_colour_list.make_record(save_path + ".txt")
    img = make_colour_barchart(uk_colour_list.array, uk_colour_list.pixel)
    img.save(save_path + "_colour.png")
    save_object(folder_colour_list, save_path)

def omit_colour_from_list(colours_list: colours_list, omit_colours: list):
    tmp_list = colours_list
    for colour in tmp_list.array:
        colour_name = colour[2]
        print(colour_name)
        for omit_colour in omit_colours:
            print(omit_colour)
            if omit_colour == colour_name:
                colours_list.delete_colours(colour)
                break
            continue

omit_colours = ["ホワイト", "ブラック", "シルバー", "ミルク・ホワイト", "スモーク・グレイ", "マウス・グレイ", "グラファイト", "グーズグレイ"]


def uk_colour_ext_hard_ristriction():
    sample_folder="/Users/yuna/Documents/GE/samples/"
    folders = glob.glob(sample_folder + "*")

    for folder in folders:
        industry = folder.replace(sample_folder,"")
        sub_category = ""
        if folder.endswith(".pickle"):
            colour_list = load_object(folder)
            omit_colour_from_list(colour_list, omit_colours)
            save_path = sample_folder + "uk_omit_BW"
            colour_list.make_record(save_path)
            img = make_colour_barchart(colour_list.array, colour_list.pixel)
            img.save(save_path + "_colour.png")
            save_object(colour_list, save_path)
        elif industry =="public":
            public_subfolders = glob.glob(folder + "/*")
            for sub_folder in public_subfolders:
                sub_category = sub_folder.replace(folder + "/", "")
                if sub_folder.endswith(".png") or sub_folder.endswith(".txt"):
                    continue
                elif sub_folder.endswith(".pickle"):
                    colour_list = load_object(sub_folder)
                    print(colour_list.array)
                    omit_colour_from_list(colour_list, omit_colours)
                    print(colour_list.array)
                    save_path = folder + "/uk_omit_BW_public"
                    colour_list.make_record(save_path)
                    img = make_colour_barchart(colour_list.array, colour_list.pixel)
                    img.save(save_path + "_colour.png")
                    save_object(colour_list, save_path)
                else:
                    files = glob.glob(sub_folder + "/*")
                    for file in files:
                        if file.endswith(".pickle"):
                            colour_list = load_object(file)
                            omit_colour_from_list(colour_list, omit_colours)
                            save_path = sub_folder + "/uk_omit_BW_" + industry + "_" + sub_category
                            colour_list.make_record(save_path)
                            img = make_colour_barchart(colour_list.array, colour_list.pixel)
                            img.save(save_path + "_colour.png")
                            save_object(colour_list, save_path)
                            break
        else:
            files = glob.glob(folder + "/*")
            for file in files:
                if file.endswith(".pickle"):
                    colour_list = load_object(file)
                    omit_colour_from_list(colour_list, omit_colours)
                    save_path = folder + "/uk_omit_BW_" + industry + "_" + sub_category
                    colour_list.make_record(save_path)
                    img = make_colour_barchart(colour_list.array, colour_list.pixel)
                    img.save(save_path + "_colour.png")
                    save_object(colour_list, save_path)
                    break

uk_colour_ext_hard_ristriction()

