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

##
