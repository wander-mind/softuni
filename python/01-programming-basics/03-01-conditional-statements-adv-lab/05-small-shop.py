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
#                         ** Small shop **
#
#    A citisen onpens some small shop in a couple of cities, and sells
# diferent stocks with diferent prices in the diferent cities.
#
#     Prices:
#     _________________________________________________________________
#    / City/Product  | Coffee  |  Water  |  Beer   | Sweets  | Peanuts \
#    |---------------|---------|---------|---------|---------|---------|
#    |    Sofia      | 0.50lv. | 0.80lv. | 1.20lv. | 1.45lv. | 1.60lv. |
#    |    Plovdiv    | 0.40lv. | 0.70lv. | 1.15lv. | 1.30lv. | 1.50lv. |
#    |    Varna      | 0.45lv. | 0.70lv. | 1.10lv. | 1.35lv. | 1.55lv. |
#    \_______________|_________|_________|_________|_________|_________/
#
#    Input:
#       1. stock    ["coffee", "water", "beer", "sweets", "peanuts"]
#       2. City     ["Sofia", "Plovdiv", "Varna"]
#       3. Amount   [0.00 - 500.00]
#
#    Output:
#       1. Price    [0.00 - 1000.00]
#

# Input
product = input()
city = input()
num = float(input())        # Quantity

# Calculation
price = 0

if city == "Sofia":
    if product == "coffee":
        price = 0.50
    elif product == "water":
        price = 0.80
    elif product == "beer":
        price = 1.20
    elif product == "sweets":
        price = 1.45
    elif product == "peanuts":
        price = 1.60
elif city == "Plovdiv":
    if product == "coffee":
        price = 0.40
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.15
    elif product == "sweets":
        price = 1.30
    elif product == "peanuts":
        price = 1.50
elif city == "Varna":
    if product == "coffee":
        price = 0.45
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.10
    elif product == "sweets":
        price = 1.35
    elif product == "peanuts":
        price = 1.55

tp = num * price            # Total price

# Output
print(f"{tp:.2f}")
