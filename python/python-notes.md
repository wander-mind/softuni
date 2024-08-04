```ascii
########################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:.       ██╗    ██╗ █████╗ ███╗   ██╗██████╗ ███████╗██████╗        .:#
#:.       ██║    ██║██╔══██╗████╗  ██║██╔══██╗██╔════╝██╔══██╗       .:#
#:.       ██║ █╗ ██║███████║██╔██╗ ██║██║  ██║█████╗  ██████╔╝       .:#
#:.       ██║███╗██║██╔══██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗       .:#
#:.       ╚███╔███╔╝██║  ██║██║ ╚████║██████╔╝███████╗██║  ██║       .:#
#:.        ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝       .:#
#:.                                                                  .:#
#:.       ███╗   ███╗██╗███╗   ██╗██████╗    E-Mail: w.m@tuta.com    .:#
#:.       ████╗ ████║██║████╗  ██║██╔══██╗                           .:#
#:.       ██╔████╔██║██║██╔██╗ ██║██║  ██║   GitHub: github.com/     .:#
#:.       ██║╚██╔╝██║██║██║╚██╗██║██║  ██║              wander-mind  .:#
#:.       ██║ ╚═╝ ██║██║██║ ╚████║██████╔╝                           .:#
#:.       ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝      Site: wandermind.xyz  .:#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
########################################################################
```

If you want to learn anything about python from my lecture notes, or you need to refresh some of your knowlege, you have to already know some python, because in these notes I will be going into detail only for the things I need, and may glimpse over or even skip some esentials. Thank you!

# 01. Basic commands

- **print({content})**
    Prints the content on the console.

- **# Comment**
    Comments start with a '#'.

- **Variable = int(input())**
    Input from user, we can set a specific type if we want, and we assign it to a variable.
    **NOTE!** When rounding *float* to *int* it always rounds to the lower whole number.
        Example: ```float 3.99 = int 3```

- **Print untill specific digit** ```print(f"{variable:.2f}")``` - print in format [0.00]
    Prints a number variable to the second digit after the decimal poinnt. Unlike when converting from *float* to *int* when it rounds to the lower number, here it rounds properly.
        Example: ```a = 1.23456789 ; print(f"{a:.4f}") ; # Prints 1.235```

- **Print in time/hours format** ```print(f"hours % 24:2d}:{minutes:02d}")``` [0:00 - 23:59]
    In this example, we format two integers into hour and minute format, where in the first part we make it so if we go over the 23 hours mark, we start over from 0'o clock, and if the hours are < 10 - we dont add a zero on front for the output format. For the minutes, we have already divided modaly by 60, so they will always be 0-59 in this case, and if the minutes < 10 - then we write in format 04 minutes for example.
        Example:
```python
total-minutes = 719
hours = total-minutes // 60 # We divide modaly to get the whole integer, not the floating point that's rest after the divission, in this case 11.
minutes = total-minutes % 60 # We get 59, as that are the minutes left after the number of hours.
print(f"{hours % 24:2d}:{minutes:02d}") # 11:59
```

- **Store time/hours as a string** ```formatted-time = f"{hours % 24:02d}:{minutes % 60:02d}" ; print(formatted-time)```
    We have stored the formated time as a string, for e.g. *9:01*, and we can use it later, in this example - to print it.

- **Print characters using numbers** ```for i in range(0, 256): print(chr(i))```
    `chr(num)` is a built-in function that takes an *integer* and returns the corresponding character from the Unicode character set.
        Example:
```python
print(chr(65))      # Output: 'A'
print(chr(97))      # Output: 'a'
print(chr(8364))    # Output: '€'
print(chr(48))      # Output: '0'
print(chr(122))     # Output: 'z'
print(chr(9829))    # Output: '♥'
```

## 01. Escape sequences

**I will add extra backslashes to escape the escape sequences in MarkDown too**. If this document is converted from *.md* to *.pdf*, or *.html* - you won't see them.

| **Escape Sequence**   | **Represents**    |
|-----------------------|-------------------|
|           \\'         |	Single Quote    |
|           \\\\        |   Backslash       |
|           \\n         |   New Line        |
|           \\r         |   Carriage Return |
|           \\t         |   Tab             |
|           \\b         |   Backspace       |
|           \\f         |   Form Feed       |
|           \\ooo       |   Octal value     |
|           \\xhh       |   Hex value       |

* Carriege return - unlike *New line*, splits 1 output into 2 new outputs (each on a new line of course).

* Form feed - Useless in these days, used for old terminals, and printes.

* Backspace - deletes the previous character.

* Octal value - A backslash followed by three integers.
    ```txt = "\110\145\154\154\157" # Hello```

* Hex value - A backslash followed by an 'x' and a hex number.
    ```txt = "\x50\x79\x74\x68\x6f\x6e" # Python```

## 02. Number Formatting

### Round UP/DOWN numbers

```python
import math #!!!!!!!!!!!!!!1

up = math.ceil(23.45)       # 24
down = math.floor(23.45)    # 23
```

### Absolute number value

```python
example1 = abs(-69)         # 69
example2 = abs(69)          # 69
```

### Rounding decimal number values

```python
# Rounding to the 3rd decimal point
rounded = round(12.3456789, 3)      # 12.346

# Formatting to the 3rd decimal point
print(f"{123.456789:.3f}")          # prints 123.457

# !! DIFERENCE BETWEEN ROUNDING & FORMATTING
print(round(35.700000, 4))          # prints 35.7
print(f"{35.700000:.4f}")           # prints 35.7000
```

### Minumum and Maximum values between 2 numbers

```python
a = 5
b = 7
x = min(a, b)   # 5         x will get the lower of the 2 valies, in this case 5 < 7, so 5
y = max(a, b)   # 7         y will get the higher of the 2 values, 7 > 5
```

### Min & Max system size

```python
import sys

smallest = sys.maxsize      # we will be compairin bumbers to this max value, the smallest gets recorded as the variables last value
biggest = -sys.maxsize      # same thing, in reverse
n - int(input())            # how many times to prompt for number input

for i in range(0, n):
    num = int(input())

    if num < smallest:
        smallest = num
    if num > biggest:
        biggest = num

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
```

## Logical operators **and**, **or**, **not**, & **in**

Operators that combine or exclude conditions.

- and - checks true for both conditions.
- or - checks if eather/or one or the other condition is true, or both.
- not - checks in the proceeding conditions is false/invalid.
- in - checks if variable is equal to one of the items in an array.

```python
a = int(input())

if a > 5 and a < 10 and a % 2 == 0: ....
if 5 < a < 10 and a % 2 == 0 ...        # same as above

if a > 5:               # \
    if a < 10:          # => same as above 2
        if a % 2 ==0:   # /

if a == 4 + 1 or a == 2 + 3, or a == 90 // 7: ... # True if any one statement is true

valid = number > 10 and number % 2 == 0 # valid becomes a bool variable, true or false
if not valid:
    print("Invalid!")

#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
animal = 'dog'

if animal in ['cat', 'dog', 'human']
    print('Mammal')
```

## 03. **for** loops

Used to repeat the same commands a sertaint number of times.

```python
for i in range(1, 13):      # iterates from 1 (inclusively) to 12 (inclusively)
    print(i)                # prints 1/n2/n3/n...12

for i in range(4, 100, 4):  # iterates from 4 to 100, adding 4 to i every time
    print(i)                # prints 4, 8, 12...96

for i in range(100, 4, -4): # iterates from 100 to 4, subtracting 4 from i every time
    print(i)                # prints 100, 96, 92...8
```

## 04. Strings

```python
# We can get the lenght of text:
text = 'Wander-Mind'
length = len(text)          # 11, counts the number of characters in the string

# We can get a specific simbol/char from text by index
letter = text[7]            # M, counts from 0, 1, 2, 3....
                            # 0 1 2 3 4 5 6|7|8 9 10
                            # W a n d e r -|M|i n d
```

### Example program 1:

Write a program that reads text/string, & prints every symbol/char on a new line.

```python
word = input()

for i in range(0, len(word)):   # Begin from letter 1 (0), and end at last character
    print(word[i])              # Prints every letter, one at a time on a new line
```

### Example program 2:

Write a program that reads a word/text/string, & prints the sum for a score if a = 1, e = 2, i = 3, o = 4, u = 5. For example: 'wander-mind' -> 6 (a+e+i = 1+2+3 = 6)

- Method 1:

```python
word = input()
sum = 0                     # We have to declare 'sum' before hand, because
                            # we may not have any of those letters, and we
                            # can't print a non-declared variable.
for i in range(0, len(word))
    if text[i] == "a":
        sum += 1
    if text[i] == "e":
        sum += 2
    if text[i] == "i":
        sum += 3
    if text[i] == "o":
        sum += 4
    if text[i] == "u":
        sum += 5

print(sum)
```

- Method 2:
```python
word = input()

vowel_values = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
sum = sum(vowel_values[char] for char in word if char in vowel_values)

print(sum)
```

- Method 3:

```python
word = input()

vowel_values = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
sum = 0

for char in word:
    if char in vowel_values:
        sum += vowel_values[char]

print(sum)
```

## 05. While loops

Example:
```python
a = 5
while a <= 10:
    print("a = " + str(a))  # Prints a = 5, a = 6, a = 7, a = 8, a = 9, a = 10
    a += 1
```

### End while loop with **break**

```python
while True:         # Endless while loop
    print("loop")
    if ...:
        break       # Breaks the endless while loop
```
