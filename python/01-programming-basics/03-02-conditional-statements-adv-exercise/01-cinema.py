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
#                             ** Cinema **
#
#    In a cinema lounge the seats are aranged in a regtanle style with
# 'r' rows and 'c' columns. There are 3 types of projections with tick-
# ets at a diferent price from eachother:
#
#    - Premiere - 12.00lv
#    - Normal - 7.50lv
#    - Discount - for children, and students - 5.00lv
#
#    Write a program that reads the type of projection (text), number of
# rows, and number of columns, entered by the user, and calculates the
# revenue from the ticket sales if the cinema is sold out. The result
# has to be printed in format [0.00].
#
#    Input:
#       1. Type of projection [Premiere, Normal, Discount]
#       2. Rows of seats (whole number)
#       3. Columns of seats (whole number)
#
#    Output:
#       1. [0.00] leva
#

# Input
tp = input()                    # Type of projection
rs = int(input())               # Rows of seats
cs = int(input())               # Columns of seats

# Calculation
price = 0

if tp == 'Premiere':            #
    price = 12.00               #
if tp == 'Normal':              #
    price = 7.50                #
if tp == 'Discount':            #
    price = 5.00                # Ticket prices

tr = price * rs * cs            # Total revenue = price * num of seats

# Output
print(f"{tr:.2f} leva")
