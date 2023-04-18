from cnc import convert

chineseNumber = [
    ["零", "0"],
    ["一", "1"],
    ["十", "10"],
    ["十二", "12"],
    ["一百", "100"],
    ["一百一", "110"],
    ["兩百零二", "202"],
    ["三零五", "305"],
    ["九百九十三", "993"],
    ["一千", "1000"],
    ["一千零一", "1001"],
    ["一千一", "1100"],
    ["一仟一", "1100"],
    ["二零一二", "2012"],
    ["三千零三", "3003"],
    ["三千零三十", "3030"],
    ["三千三百", "3300"],
    ["三千三", "3300"],
    ["四千五", "4500"],
    ["一萬", "10000"],
    ["一萬零一", "10001"],
    ["一萬一", "11000"],
    ["一萬零五百", "10500"],
    ["六万七", "67000"],
    ["8萬1", "81000"],
    ["十萬零一", "100001"],
    ["十萬一", "101000"],
    ["十萬三千", "103000"],
    ["12萬9000", "129000"],
    ["三百萬", "3000000"],
    ["三百一十三萬零四十", "3130040"],
    ["九八七萬零五百", "9870500"],
    ["四千零五萬七千八百零九", "40057809"],
    ["五百零七萬四千", "5074000"],
    ["六千零三萬", "60030000"],
    ["九千三百零七萬五十", "93070050"],
    ["一億一萬一千零三", "100011003"],
    ["九億三千零五十六", "900003056"],
    ["三百零五億零五百零二", "30500000502"],
    ["一兆零一十六", "1000000000016"],
    ["十兆三千億五十七萬零九", "10300000570009"],
    ["一千零七十六兆五百億四千零七十二萬三千五百一十二", "1076050040723512"],
    ["5000億4321萬987", "500043210987"],
    ["四千兆零三", "4000000000000003"],
    ["廿", "20"],
    ["圩一", "51"],
    ["卅二", "32"],
    ["皕樺捌", "298"],
    ["三千枯", "3080"],
    ["念萬玖仟柒佰卌肆", "209744"],
    ["圓億零三", "6000000003"]
]

numberChinese = [
    ["0", "零"],
    ["1", "一"],
    ["10", "十"],
    ["12", "十二"],
    ["22", "二十二"],
    ["57", "五十七"],
    ["100", "一百"],
    ["103", "一百零三"],
    ["202", "兩百零二"],
    ["222", "兩百二十二"],
    ["320", "三百二十"],
    ["304", "三百零四"],
    ["420", "四百二十"],
    ["678", "六百七十八"],
    ["1000", "一千"],
    ["1001", "一千零一"],
    ["1010", "一千零一十"],
    ["1100", "一千一百"],
    ["2002", "兩千零二"],
    ["2202", "兩千兩百零二"],
    ["2222", "兩千兩百二十二"],
    ["5000", "五千"],
    ["9030", "九千零三十"],
    ["10000", "一萬"],
    ["12111", "一萬兩千一百一十一"],
    ["12001", "一萬兩千零一"],
    ["12010", "一萬兩千零一十"],
    ["12345", "一萬兩千三百四十五"],
    ["22222", "兩萬兩千兩百二十二"],
    ["40404", "四萬零四百零四"],
    ["55005", "五萬五千零五"],
    ["50520", "五萬零五百二十"],
    ["100000", "十萬"],
    ["100005", "十萬零五"],
    ["100050", "十萬零五十"],
    ["100500", "十萬零五百"],
    ["105000", "十萬五千"],
    ["110000", "十一萬"],
    ["112000", "十一萬兩千"],
    ["222002", "二十二萬兩千零二"],
    ["1002000", "一百萬兩千"],
    ["2027846", "兩百零二萬七千八百四十六"],
    ["70090202", "七千零九萬零兩百零二"],
    ["90003045", "九千萬三千零四十五"],
    ["100000000", "一億"],
    ["200000000", "兩億"],
    ["4030106022", "四十億三千零一十萬六千零二十二"],
    ["5022001930", "五十億兩千兩百萬一千九百三十"],
    ["90980087007", "九百零九億八千零八萬七千零七"],
    ["123456789009", "一千兩百三十四億五千六百七十八萬九千零九"],
    ["200200022002", "兩千零二億零兩萬兩千零二"],
    ["1202994070004032", "一千兩百零二兆九千九百四十億七千萬四千零三十二"]
]

for s in chineseNumber:
    r = convert.chinese2number(s[0])
    if r != int(s[1]):
        print(s[0], "/", str(r))


for s in numberChinese:
    r = convert.number2chinese(int(s[0]))
    if r != s[1]:
        print(s[0], "/", str(r))