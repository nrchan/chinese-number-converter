# chinese-number-convertor

This is a simple Chinese number converter that converts between [Chinese numberals](https://en.wikipedia.org/wiki/Chinese_numerals) and [arabic numbers](https://en.wikipedia.org/wiki/Arabic_numerals).

## 👍Quickstart

```python
from cnc import convert

print(convert.chinese2number("五十七")) #57
print(convert.number2chinese(57)) #五十七
```

## 👉chinese2number(string) -> (float|int)

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

## 👉number2chinese(int) -> (string)

Returns the chinese representation of given number.

### Arguments

- **language**: "**T**" or "**S**". Choose between Traditional and Simplified characters. (default is "T")
- **bigNumber**: bool, **True** or **False**. Output capital version of charaters. (default is False) 

### Notes

This function uses "萬進" logic when dealing with larger number (> 10<sup>8</sup>), which basically means that every 4 digits will be treated as a group.
This is the most common logic to deal with large numbers, and can support up to 10<sup>52</sup>-1.