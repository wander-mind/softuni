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
#                          ** New house **
#
#    John and Jane are buing a house together. Jane loves flowers so mu-
# ch, that she convinces you to write a program, that calculates how mu-
# ch it will cost them to plant a certain number of flowers, and if the
# budget they have will be enough. Diferent flowers have diferent prices
#
# /--------------------------------------------------------------------\
# |     Flower     |  Rose  | Dahlia |  Tulip  | Narcissus | Gladiolus |
# |----------------|--------|--------|---------|-----------|-----------|
# |Price per flower| 5.00lv | 3.80lv | 2.80lv  |  3.00lv   |  2.50lv   |
# \--------------------------------------------------------------------/
#
#    Discounts:
#       - More than 50 Roses        - 10% off of the final price.
#       - More than 90 Dahlias      - 15% off of the final price.
#       - More than 80 Tulips       - 15% off of the final price.
#       - Less than 120 Narcissus   - 15% extra on the final price.
#       - Less than 80 Gladiolus    - 20% extra on the final price.
#
#    Input:
#       1. Flower type [Roses, Dahlias, Tulips, Narcissus, Gladiolus]
#       2. Number of flowers (whole number)
#       3. Budget (whole number)
#
#    Output:
#       1. If the budget is enough:
#           - "Hey, you have a great garden with {number of flowers}
#              {flower type} and {money left [0.00]} leva left."
#       2. If the budget is NOT enough:
#           - "Not enough money, you need {$ needed [0.00]} leva more."
#

# Input
ft = input()                    # Flower type
fn = int(input())               # Flower number
bud = int(input())              # Budget

# Calculation
price = 0

if ft == "Roses":
    price = fn * 5              # Total price for the flowers
    if fn > 50:
        price *= 0.9            # Discount

elif ft == "Dahlias":
    price = fn * 3.8            # Total price for the flowers
    if fn > 90:
        price *= 0.85           # Discount

elif ft == "Tulips":
    price = fn * 2.8            # Total price for the flowers
    if fn > 80:
        price *= 0.85           # Discount

elif ft == "Narcissus":
    price = fn * 3              # Total price for the flowers
    if fn < 120:
        price *= 1.15           # Extra charge

elif ft == "Gladiolus":
    price = fn * 2.5            # Total price for the flowers
    if fn > 80:
        price *= 1.2            # Extra charge

# Output
if bud >= price:
    ml = bud - price            # Money left
    print(f"Hey, you have a great garden with {fn} {ft} and {ml:.2f} " +
          "leva left.")
else:
    mn = price - bud            # Money needed
    print(f"Not enough money, you need {mn:.2f} leva more.")
