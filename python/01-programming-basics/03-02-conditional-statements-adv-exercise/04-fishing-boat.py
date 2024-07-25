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
#                          ** Fishing boat **
#
#    Tony and his friends love fishing soooooo much, that they decide to
# go fishing with a ship. Price for renting that ship varies based on
# the season and the number of fishermen. Write a program that calcula-
# tes if they will have enough money for renting the ship.
#
#    Based on the season:
#       - Spring                - 3000lv
#       - Summer and Autumn     - 4200lv
#       - Winter                - 2600lv
#
#    Based on the number of fishermen:
#       - up to 6 ppl included              - 10% discount
#       - between 7 and 11 ppl included     - 15% discount
#       - over 12 ppl                       - 25% discount
#
#    The fishermen use and extra 5% discount on top if their number is
# even, but only if the season isn't Autumn.
#
#    Input:
#       1. Budget (whole number)
#       2. Season [Spring, Summer, Autumn, Winter]
#       3. Number of fishermen (Whole number)
#
#    Output:
#       1. If the budget is enough:
#           - "Yes! You have {money left [0.00]} leva left."
#          If the budget is NOT enough:
#           - "Not enough money! You need {money needed [0.00]} leva."
#

# Input
bud = int(input())              # Budget
s = input()                     # Season
nf = int(input())               # Number of fishermen

# Calculation
srp = {                         # Ship rental prices
    "Spring": 3000,
    "Summer": 4200,
    "Autumn": 4200,
    "Winter": 2600
    }

sp = srp[s]                     # Ship price (based on the season)

if nf <= 6:
    sp *= 0.9                   # Ship price after 10% discount
elif 6 < nf < 12:
    sp *= 0.85                  # Ship price after 15% discount
else:
    sp *= 0.75                  # Ship price after 25% discount

if nf % 2 == 0 and s != 'Autumn':
    sp *= 0.95                  # Extra 5% discount if 'fn' are even num

# Output
if bud >= sp:
    ml = bud - sp               # Money left if budget is enough
    print(f"Yes! You have {ml:.2f} leva left.")
else:
    mn = sp - bud               # Money needed in budget is NOT enough
    print(f"Not enough money! You need {mn:.2f} leva.")
