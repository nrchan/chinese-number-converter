# chinese-number-convertor

This is a simple Chinese number converter that converts between [Chinese numberals](https://en.wikipedia.org/wiki/Chinese_numerals) and [arabic numbers](https://en.wikipedia.org/wiki/Arabic_numerals).

## 👍 Quickstart

```python
from cnc import convert

print(convert.chinese2number("五十七")) #57
print(convert.number2chinese(57)) #五十七
```

## 👉 chinese2number(string) -> (float|int)

Returns the arabic number representation of given string.

### Notes

The function uses a loosely-matching logic, so the given string doesn't need to be confined to a specific pattern.

```python
print(convert.chinese2number("兩千零一十二")) #2012
print(convert.chinese2number("二零一二")) #will also be 2012
print(convert.chinese2number("2012")) #will be, of course, 2012
```
> That being said, please still avoid ambiguous and grammartically incorrect string such as ```一兆一``` or ```一百一千億```.

### Support character

Support following characters:
- **Normal number**: 一...九、十、百、千
- **Large number** till 10<sup>52</sup>-1: 萬、億...極
- **Zero**: 零、〇
- **Captial version** of all characters above: 壹...玖、拾、佰、仟
- **Arabic number**: 1...9、0
- **Simplified version** off all characters above: 贰、万...
> Arabic numbers were also supported because they will sometimes be mixed with characters, like "1億5000萬".

## 👉 number2chinese(int) -> (string)

Returns the chinese representation of given number.

### Arguments

- **language**: string, "**T**" or "**S**". Choose between Traditional and Simplified characters. (default is "T")
- **bigNumber**: bool, **True** or **False**. Output capital version of charaters. (default is False)

```python
print(convert.number2chinese(202)) #兩百零二
print(convert.number2chinese(202, language = "S", bigNumber = True)) #贰佰零贰
```

- **forceErLian**: string, **auto**, **force** or **forceNot**. Whether to distinguish Er(二) and Lian(两). When set to "auto", the output will follow regional convention. When set to "force", both Traditional and Simplified version will distinguish word usage, while "forceNot" will always output Er(二) for number "two". (default is "auto")
> This will only effect when not using capital number (bigNumber = False). Using capital number will always output 貳/贰.

```python
print(convert.number2chinese(202, language = "T")) #兩百零二
print(convert.number2chinese(202, language = "T", forceErLian = "forceNot")) #二百零二
print(convert.number2chinese(202, language = "S")) #二百零二
print(convert.number2chinese(202, language = "S", forceErLian = "force")) #两百零二
```

### Notes

This function uses "萬進" logic when dealing with larger number (> 10<sup>8</sup>), which basically means that every 4 digits will be treated as a group.
This is the most common logic to deal with large numbers, and can support up to 10<sup>52</sup>-1.