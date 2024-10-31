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
#
#                        ** Fruits shop **
#
#    A fruits shop has these prices during the work-week:
#  /------------------------------------------------------------------\
# / fruit | banana | apple | orange |grapefruit| kiwi |pineapple| grape\
# |-------|--------|-------|--------|----------|------|---------|------|
# \ price | 2.50   | 1.20  | 0.85   | 1.45     | 2.70 | 5.50    | 3.85 /
#  \______|________|_______|________|__________|______|_________|_____/
#
#    During the weekend, the shops works with higher prices:
#  /------------------------------------------------------------------\
# / fruit | banana | apple | orange |grapefruit| kiwi |pineapple| grape\
# |-------|--------|-------|--------|----------|------|---------|------|
# \ price | 2.70   | 1.25  | 0.90   | 1.60     | 3.00 | 5.60    | 4.20 /
#  \______|________|_______|________|__________|______|_________|_____/
#
#    Write a program that reads from the console 3 variables, entered by
# the user, and calculates the price.
#
#    Input:
#       1. Fruit name
#       2. Day of the week [Monday ... Sunday]
#       3. Amount (R) [0.00 - 100.00]
#
#    Output:
#       1. Price (R) [0.00]
#

# Input
fn = input()                # Fruit name
dw = input()                # Day of the week
af = float(input())         # Amount of fruit

# Calculation
price = 0

if dw in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fn == "banana":
        price = 2.50
    elif fn == "apple":
        price = 1.20
    elif fn == "orange":
        price = 0.85
    elif fn == "grapefruit":
        price = 1.45
    elif fn == "kiwi":
        price = 2.70
    elif fn == "pineapple":
        price = 5.50
    elif fn == "grapes":
        price = 3.85

elif dw in ["Saturday", "Sunday"]:
    if fn == "banana":
        price = 2.70
    elif fn == "apple":
        price = 1.25
    elif fn == "orange":
        price = 0.90
    elif fn == "grapefruit":
        price = 1.60
    elif fn == "kiwi":
        price = 3.00
    elif fn == "pineapple":
        price = 5.60
    elif fn == "grapes":
        price = 4.20

if price > 0:
    tp = af * price         # Total price

# Output
print(f"{tp:.2f}")
