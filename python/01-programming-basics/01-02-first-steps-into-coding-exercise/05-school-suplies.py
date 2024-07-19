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
#                         ** School suplies **
#
#    School has started and Anne is class president. She has to buy a
# sertain number of pens, markers, and whiteboard cleaner. She is a re-
# gular customer at the supplies shop, so she has a discount, which is
# a sertaint amount of the total price. Write a program that calculates
# how much money Anne has to save in order to pay, knowing this:
#
#	- pens - 5.80lv.
#	- markers - 7.20lv.
#	- cleaner - 1.20lv. per liter.
#
#    Input:
#	1. Pens [0-100]
#	2. Markers [0-100]
#	3. Cleaner [0-50]
#	4. Discount % [0-100]
#
#    Output:
#	1. End price
#

# Input
pens = int(input())
markers = int(input())
cleaner = int(input())
discount = int(input())

# Calculation
totalPrice = pens * 5.80 + markers * 7.20 + cleaner * 1.20
finalPrice = totalPrice - totalPrice * (discount / 100)

# Output
print(f"{finalPrice:.2f}")
