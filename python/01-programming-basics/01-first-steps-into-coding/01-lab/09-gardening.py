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
#                          ** Yard greening **
#
#    Cate has a couple of houses near the beach and wants to green up
# some of their yards, making them welcoming for her guests. She has
# rented a company for the job.
#
#    Write a program that calculates the total sum which Cate will have
# to pay the firm. The price per m^2 is 7.61lv (tax included). Since
# she has a lot of properties, she gets an 18% discount for the job.
#
#    Input:
#	1. Square meters of land [0.00-10000.00]
#
#    Output:
#	1. "The final price is: {end price} lv."
#	2. "The discount is: {discounted amount} lv."
#

# Input:
area = float(input())

# Calculation:
price = area * 7.61
discount = price * 0.18
total = price - discount

# Output:
print(f"The final price is: {total:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")

# In both outputs we round the prices to their second decimal.
