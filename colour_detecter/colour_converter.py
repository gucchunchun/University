import numpy as np
import math

def hex_to_rgb(hex):
  r = int(hex[0:2], 16)
  g = int(hex[2:4], 16)
  b = int(hex[4:6], 16)
  
  return (r, g, b)

class rgb_converter():
  def __init__(self,r, g, b):
    self.r = r
    self.g = g
    self.b = b
    self.rgb = (r, g, b)
    self.srgb = self.rgb_srgb()
    self.xyz = self.srgb_xyz()
    self.lab = self.xyz_lab()

  #setting: D65 illuminant
  #reference: https://kibata-ai-labo.com/programming/convert_srgb2lab/
  #reference: http://yamatyuu.net/other/color/cie1976lab/index.html
  #reference: https://note.com/yoshicolor/n/n5b9a78e186f0
  #reference: http://www.psy.ritsumei.ac.jp/~akitaoka/RGBtoXYZ_etal01.html
  def rgb_srgb(self):
    #γ2.2
    sR = math.pow((self.r/255), 2.2)
    sG = math.pow((self.g/255), 2.2)
    sB = math.pow((self.b/255), 2.2)
    return (sR, sG, sB)
 
  def srgb_xyz(self):
    XYZ_MATRIX = [
             [0.412391, 0.357584, 0.180481],
             [0.212639, 0.715169, 0.072192],
             [0.019331, 0.119195, 0.950532]
            ]
    
    linear_array = []
    for value in self.rgb:
      if value/255 <= 0.04045:
        linear_array.append(value/255/12.92)
      else:
        linear_array.append(math.pow((value/255 + 0.055)/1.055, 2.4))

    #*100=%
    xyz = []
    for matrix in XYZ_MATRIX:
      value = 0
      for i in range(0,3):
        value  += linear_array[i] * matrix[i]
      xyz.append(value)
    return tuple(xyz)
  
  def xyz_lab(self):
    def trans_function(argument):
      if argument > math.pow(24/116, 3):
        return math.pow(argument, 1/3)
      else:
        return 841/108 * argument + 16/116
    Xn = 0.95039
    Yn = 1.0
    Zn = 1.0888

    l = 116 * trans_function(self.xyz[1]/Yn) - 16
    a = 500 * (trans_function(self.xyz[0]/Xn)-trans_function(self.xyz[1]/Yn))
    b = 200 * (trans_function(self.xyz[1]/Yn)-trans_function(self.xyz[2]/Zn))
    return (l, a, b)


#colour convert module