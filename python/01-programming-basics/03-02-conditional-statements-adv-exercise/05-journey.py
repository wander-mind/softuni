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
#                              ** Journey **
#
#    A young programmer has a sertain budget, and time free time in a
# given season. Write a program, that calculates what kind of vacation
# spot he can afford and how much it will cost him. The budget defines
# the destination, and the season - how much he will spend from that bu-
# dget.
#
#    If the season is Summer, he will vacate in a camping. If the season
# is Winter - hotel. If in Europe, no matter the season, he will be in a
# hotel. Every camping place or hotel, based on the destination, has its
# own price, which corresponds as a % of the budget.
#
#    - If the budget is 100lv or less - somewhere in Bulgaria:
#       - Summer - 30% of the budget.
#       - Winter - 70% of the budget.
#
#    - If the budget is 1000lv or less - somewhere in the Balkans:
#       - Summer - 40% of the budget.
#       - Winter - 80% of the budget.
#
#    - If the budget is more than 1000lv - somewhere in Europe:
#       - No matter the season, he will spend 90% of the budget.
#
#    Input:
#       1. Budget (R) [0.00 - 10000.00]
#       2. Season ["summer", "winter"]
#
#    Output:
#       1. print "Somewhere in {["Bulgaria", "Balkans", "Europe"]}"
#       2. print "{["Camp", "Hotel"]} - {money spent [0.00]}"
#

# Input
bud = float(input())                # Budget
s = input()                         # Season

# Calculation
#####################################
if bud <= 100:
    des = "Bulgaria"                # Destination

    if s == "summer":
        vt = "Camp"                 # Vacation type
        ms = bud * 0.3              # Money spent

    elif s == "winter":
        vt = "Hotel"
        ms = bud * 0.7

#####################################
elif 100 < bud <= 1000:
    des = "Balkans"

    if s == "summer":
        vt = "Camp"
        ms = bud * 0.4

    elif s == "winter":
        vt = "Hotel"
        ms = bud * 0.8

#####################################
elif 1000 < bud:
    des = "Europe"
    vt = "Hotel"
    ms = bud * 0.9

#####################################
# Output
print(f"Somewhere in {des}")
print(f"{vt} - {ms:.2f}")
