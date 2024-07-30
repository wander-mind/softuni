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

# **01. Programming basics**

## 01. First steps into coding

If you want to learn anything about python from my lecture notes, or you need to refresh some of your knowlege, you have to already know some python, because in these notes I will be going into detail only for the things I need, and may glimpse over or even skip some esentials. Thank you!

### Basic commands

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
        Example: ```a = 1.23456789 ; print(f"{a:.3f}") ; # Prints 1.235```

- **Print in time/hours format** ```print(f"hours % 24:2d}:{minutes:02d}")``` [0:00 - 23:59]
    In this example, we format two integers into hour and minute format, where in the first part we make it so if we go over the 23 hours mark, we start over from 0'o clock, and if the hours are < 10 - we dont add a zero on front for the output format. For the minutes, we have already divided modaly by 60, so they will always be 0-59 in this case, and if the minutes < 10 - then we write in format 04 minutes for example.
        Example:
        ```Python
        total-minutes = 719
        hours = total-minutes // 60 # We divide modaly to get the whole integer, not the floating point that's rest after the divission, in this case 11.
        minutes = total-minutes % 60 # We get 59, as that are the minutes left after the number of hours.
        print(f"{hours % 24:2d}:{minutes:02d}") # 11:59
        ```

- **Store time/hours as a string** ```formatted-time = f"{hours % 24:02d}:{minutes % 60:02d}" ; print(formatted-time)```
    We have stored the formated time as a string, for e.g. *9:01*, and we can use it later, in this example - to print it.
