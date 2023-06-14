#データの型
print(2)        
print(5.5)       
print('Saitama')   
print(False)      

print(type(3))
print(type(3.0))
print(type('Tokyo'))
print(type(True))

#演算子による数値計算 & 優先順位
print(3 + 5) 
print(5 - 3) 
print(7 * 8) 
print(14 / 3) 
print(14 // 3) 
print(14 % 3) 
print(2 ** 3) 

print(58 - 4 * 8)
print((58 - 4) * 8)


#整数型と浮動小数点が混ざった計算
print(3 + 4)
print(3 + 4.0)
print(3.0 + 4.0)
print(type(3 + 4))
print(type(3 + 4.0))
print(type(3.0 + 4.0))

print(6 / 4)
print(6 / 3)
print(6 // 3)
print(6 / 3.0)
print(6.0 / 3.0)

#数値計算の誤差
print(0.1)
print(0.2)
print(0.7)
print(0.1 + 0.2)
print(0.1 + 0.7)
print(0.7 - 0.2)

print(0.1 + 0.2)
print(round(0.1 + 0.2, 4))
print(int(0.1 + 0.2))
print(int((0.1 + 0.2) * 10))
print(0.1 + 0.7) #0.7999999999999999
print(round(0.1 + 0.7, 3)) #0.8
print("int(): ", int(0.1 + 0.7)) #0
print("int(*10): ", int((0.1 + 0.7) * 10)) #7
print("int(*100): ", int((0.1 + 0.7) * 100)) #80
print("int(*1000): ", int((0.1 + 0.7) * 1000)) #800

print(0.7 - 0.2)
print(round(0.7 - 0.2, 1))
print("int(*10): ", int((0.7 - 0.2) * 10)) #4.999...4
print("int(*100): ", int((0.7 - 0.2) * 100)) #49.9999...4
print("int(*1000): ", int((0.7 - 0.2) * 1000)) #499.99...4

print(1 / 3) #0.3333...
print("int(): ", int(1 / 3 * 3)) #0.99999...=0
print("int(*10): ", int((1 / 3 * 3) * 10)) #9.99999...=9
print("int(*100): ", int((1 / 3 * 3) * 100)) #99.99999...=99

#誤差が出るのは浮動小数は、仮数・基数・指数を用いて表現するため
print( format(0.2, '.55f') )
print( format(0.7, '.55f') )
print( format(0.9, '.55f') )


