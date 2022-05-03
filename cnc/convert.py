import math

ChineseNumber2Number = {
    "1": 1,
    "一": 1,
    "壹": 1,
    "2": 2,
    "二": 2,
    "貳": 2,
    "貮": 2,
    "兩": 2,
    "3": 3,
    "三": 3,
    "叁": 3,
    "參": 3,
    "叄": 3,
    "4": 4,
    "四": 4,
    "肆": 4,
    "5": 5,
    "五": 5,
    "伍": 5,
    "6": 6,
    "六": 6,
    "陸": 6,
    "7": 7,
    "七": 7,
    "柒": 7,
    "8": 8,
    "八": 8,
    "捌": 8,
    "9": 9,
    "九": 9,
    "玖": 9,
    "0": 0,
    "零": 0,
    "〇": 0
}   

ChineseUnit2Number = {
    "十": 10,
    "拾": 10,
    "百": 100,
    "佰": 100,
    "千": 1000,
    "仟": 1000
}

ChineseBigUnit2Number = {
    "萬": 1e+4,
    "億": 1e+8,
    "兆": 1e+12,
    "京": 1e+16,
    "垓": 1e+20,
    "秭": 1e+24,
    "穰": 1e+28,
    "溝": 1e+32,
    "澗": 1e+36,
    "正": 1e+40,
    "載": 1e+44,
    "極": 1e+48
}

ChineseUnit = [
    "",
    "十",
    "百",
    "千"
]

ChineseBigUnit = [
    "",
    "萬",
    "億",
    "兆",
    "京",
    "垓",
    "秭",
    "穰",
    "溝",
    "澗",
    "正",
    "載",
    "極"
]

Number2Chinese = {
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    6: "六",
    7: "七",
    8: "八",
    9: "九",
    0: "零"
}

class ConvertError(Exception):
    def __init__(self, what):
        self.what = what
    
    def __str__(self):
        return self.what

def chinese2number(string):
    curDigit = 0
    curNum = 0
    num = 0
    for i in range(len(string)):
        c = string[i]
        if c in ChineseNumber2Number:
            curDigit *= 10
            curDigit += ChineseNumber2Number[c]

            #for "一百一" is 110 (not 101) issue
            if i == len(string)-1 and len(string) >= 2 and string[i-1] == "百":
                curDigit *= 10
            #for "一千一" is 1100 (not 1001) issue
            if i == len(string)-1 and len(string) >= 2 and string[i-1] == "千":
                curDigit *= 100
            #for "一萬一" is 11000 (not 10001) issue
            if i == len(string)-1 and len(string) >= 2 and string[i-1] == "萬":
                curDigit *= 1000
        if c in ChineseUnit2Number:
            if curDigit == 0:
                curNum += ChineseUnit2Number[c]
            else:
                curNum += curDigit*ChineseUnit2Number[c]
            curDigit = 0
        if c in ChineseBigUnit2Number:
            curNum += curDigit
            curDigit = 0
            curNum *= ChineseBigUnit2Number[c]
            num += curNum
            curNum = 0
    curNum += curDigit
    num += curNum
    return num

def number2chinese(number):
    if number == 0:
        return "零"
    if number >= 1e+52:
        raise ConvertError("Number is too large. Maximum is (1e+52)-1.")

    string = ""
    section = []
    while number > 0:
        section.append(number%10000)
        number //= 10000
    
    previousZero = 0 #0 for not applicable, 1 for there is zero and should be print in the future, -1 for no zero

    for i in reversed(range(len(section))):
        digit = []
        for j in range(4):
            digit.append(section[i]%10)
            section[i] //= 10
        for j in reversed(range(4)):
            if digit[j] != 0:
                #for zero issue
                if previousZero == 1:
                    string += Number2Chinese[0]
                    previousZero = -1
                if previousZero == 0:
                    previousZero = -1

                #for "十" and "一十" issue
                if not(j == 1 and digit[j] == 1 and digit[2] == 0 and digit[3] == 0):
                    if (j == 2 or j == 3) and digit[j] == 2:
                        string += "兩"
                    elif j == 0 and i != 0 and digit[j] == 2 and digit[1] == 0 and digit[2] == 0 and digit[3] == 0:
                        string += "兩"
                    else:
                        string += Number2Chinese[digit[j]]
                
                string += ChineseUnit[j]
            elif digit[j] == 0:
                if previousZero == -1:
                    previousZero = 1
        
        if not(digit[0] == 0 and digit[1] == 0 and digit[2] == 0 and digit[3] == 0):
            string += ChineseBigUnit[i]
    
    return string
