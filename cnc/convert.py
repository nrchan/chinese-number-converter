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

def chinese2number(string):
    curDigit = 0
    curNum = 0
    num = 0
    for c in string:
        if c in ChineseNumber2Number:
            curDigit *= 10
            curDigit += ChineseNumber2Number[c]
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