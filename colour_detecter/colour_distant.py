import colour_converter as cc
from pyciede2000 import ciede2000
#abs = absolute value
#ユーグリット距離では人の目で感じる差を特定できない）
#ciede2000/colour distance = .delta_E_00


class colour_distant():
    colour1: tuple
    colour2: tuple

    def __init__(self, colour1RGB, colour2RGB):
        self.colour1 = colour1RGB
        self.colour2 = colour2RGB
        self.euclidean = self.euclidean_distant()
        self.ciede2000 = self.ciede2000_distant()

    def euclidean_distant(self):
        distant = abs(self.colour1[0]- self.colour2[0]) + abs(self.colour1[1]- self.colour2[1]) + abs(self.colour1[2] - self.colour2[2])
        return distant

    def ciede2000_distant(self):
        #argumrnt = tuple of rgb
        colour1lab = cc.rgb_converter(self.colour1[0],self.colour1[1],self.colour1[2]).lab
        colour2lab = cc.rgb_converter(self.colour2[0],self.colour2[1],self.colour2[2]).lab

        distant = ciede2000(colour1lab,colour2lab)["delta_E_00"]
        return distant

