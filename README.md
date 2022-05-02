# chinese-number-convertor

This is a simple Chinese number converter that converts between [Chinese numberals](https://en.wikipedia.org/wiki/Chinese_numerals) and [arabic numbers](https://en.wikipedia.org/wiki/Arabic_numerals).

## Quickstart

```python
from cnc import convert

print(convert.chinese2number("五十七")) #57
```

## chinese2number(string)

Returns the arabic number representation of given string (in type int or float).

It uses a loosely-matching logic, so the given string doesn't need to be confined to a specific pattern.

```python
print(convert.chinese2number("兩千零一十二")) #2012
print(convert.chinese2number("二零一二")) #will also be 2012
print(convert.chinese2number("2012")) #will be, of course, 2012
```

Support following characters:
- Normal number: 一...九、十、百、千
- Large number till 10^48^: 萬、億...極
- Zero: 零、〇
- Captial version of all characters above: 壹...玖、拾、佰、仟
- Arabic number: 1...9、0
> Arabic numbers were also supported because they will sometimes be mixed with characters, like "1億5000萬".