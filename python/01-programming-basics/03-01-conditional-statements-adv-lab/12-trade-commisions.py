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
#    A company is paying commisions, based the town they wirk in, and
# the amount work they do:
#  ____________________________________________________________________
# /  City  | [0 - 500] | (500 - 1000] | (1000 - 10000] | [10000 - max) \
# |--------|-----------|--------------|----------------|---------------|
# | Sofia  |     5%    |      7%      |       8%       |      12%      |
# | Varna  |    4.5%   |     7.5%     |       10%      |      13%      |
# \ Plovdiv|    5.5%   |      8%      |       12%      |     14.5%     /
#  \_______|___________|______________|________________|______________/
#
#    Write a program that reads the name of a city, entered by the user,
# and amount of sales (R), and calculates the sellers commision, based
# ont the above table. When inputing an invalid name of a city, or a ne-
# gative num of sales - print "error".

#    Input:
#       1. City (Sofia, Varna, Plovdiv)
#       2. Amount of sales (R) [0.00 - max)
#
#    Output:
#       1. Amount of commsion (R) [0.00 - max)
#

# Input
city = input()                  # City name
sales = float(input())          # Number of sales

# Calculation
com = 0                         # Commision

if city == "Sofia":
    if 0 <= sales <= 500:
        com = 0.05
    elif 500 < sales <= 1000:
        com = 0.07
    elif 1000 < sales <= 10000:
        com = 0.08
    elif sales > 10000:
        com = 0.12
    else:
        print("error")

elif city == "Varna":
    if 0 <= sales <= 500:
        com = 0.045
    elif 500 < sales <= 1000:
        com = 0.075
    elif 1000 < sales <= 10000:
        com = 0.1
    elif sales > 10000:
        com = 0.13
    else:
        print("error")

elif city == "Plovdiv":
    if 0 <= sales <= 500:
        com = 0.055
    elif 500 < sales <= 1000:
        com = 0.08
    elif 1000 < sales <= 10000:
        com = 0.12
    elif sales > 10000:
        com = 0.145
    else:
        print("error")

else:
    print("error")

if com > 0:
    tc = sales * com            # Total commision

# Output
print(f"{tc:.2f}")
