#BMI calcurator
def BMIcalculator(height, weight):
    bmi = round(float(weight) / ((float(height)/100)**2), 2)
    idealBodyWeight = round(22 * (float(height)/100)**2, 2)

    print(f"BMI: {bmi}\nIdeal body weight: {idealBodyWeight}")

# BMIcalculator(165.5,60)
#キーボードから半径rを読み込んで，その半径の円の面積と球の体積を計算して表示する
def SurfaurfaceVolume():
    radius = input("Enter radius:")
    surface = round(float(radius)**2 * 3.14, 2)
    volume = round(float(radius)**3 * 3.14 * 3 / 4, 2)

    print(f"Surface: {surface}cm2\nVolume: {volume}cm3")

# SurfaurfaceVolume()

def numberToTime():
    number = int(input("Enter any integer: "))
    day = 60**2 * 24
    hour = 60**2
    minute = 60
    days  = number // day
    hours = (number % day) // hour
    minutes = ((number % day) % hour) // minute
    seconds = ((number % day) % hour) % minute

    print(f"{number}s is {days} days and {hours}h {minutes}m {seconds}s")

# numberToTime()

def interestCal(AorB):
    if AorB == "A":
        rate = 0.20
        print("Bank A")
    elif AorB == "B":
        rate = 0.02
        print("Bank B")
    else:
        return print("Enter A or B")
    principal = int(input("Enter principal(万円): ")) * 10**4
    years = int(input("How many years: "))
    simple = int(principal * (1 + rate / 100 * years) / 10**4)
    compound = int(principal * (1 + rate / 100) * years / 10**4)

    print(f"Principal: {principal}\n\
            Years: {years}\n\
            Simple interest: {simple}万円\n\
            Compound interest: {compound}万円")

# interestCal("A")
# interestCal("B")


# s1 =("Peter Piper picked a peck of pickled peppers."\
# "A peck of pickled peppers Peter Piper picked."\
# "If Peter Piper picked a peck of pickled peppers,"\
# "Where's the peck of pickled peppers Peter Piper picked?")

# #すべて小文字に書き換えた文字列s2を作成する
# s2 = s1.lower()
# print("1: \n" + s2)

# #s1からスペースを削除する
# print("2: \n"+ s1.replace(" ",""))

# #s2からpeterの数を数える
# print("3: \n" + str(s2.count("peter")))

# #s1をすべて大文字に書き換えて文字の並び順を逆にする
# print("4: \n" + s1.upper()[::-1])

# #s2からpeppersを!!!に置き換える
# print("5: \n" + s2.replace("peppers","!!!"))

# #s1で，Ifで始まる8文字の文字列を抜き出してください
# print("6: \n" + s1[s1.find("If"):s1.find("If")+9:])
