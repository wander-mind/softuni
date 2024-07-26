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
#                          ** Hotel Room **
#
#    The hotel offers 2 types of rooms: studios and apartments. Write a
# program that calculates the price for the whole stay for a studio or
# an apartment. The prices vary based on the month:
#
# /--------------------------------------------------------------------\
# |    May & October    |    June & September    |    July & August    |
# |~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~|
# | Studio - 50lv/night | Studio - 75.20lv/night | Studio - 76lv/night |
# |- - - - - - - - - - -|- - - - - - - - - - - - | - - - - - - - - - - |
# | Apart. - 65lv/night | Apart. - 68.70lv/night | Apart. - 77lv/night |
# \--------------------------------------------------------------------/
#
#    The hotel offers these discounts:
#   - For a studio, more than 7 nights during May & October: 5% off
#   - For a studio, more than 14 nights during May & October: 30% off
#   - For a studio, more than 14 nights during June & September: 20% off
#   - For an apartment, more than 14 nights, any month: 10% off
#
#    Input:
#       1. Month [May, June, July, August, September, October]
#       2. Number of nights (whole number)
#
#    Output:
#       1. print "Apartment: {price for whole stay [0.00] lv.}"
#       2. print "Studio: {{price for whole stay [0.00] lv.}"
#

# Input
m = input()                         # Month
nn = int(input())                   # Number of nights

# Calculation
if m in ['May', 'October']:
    sp = nn * 50                    # Studio Price
    ap = nn * 65                    # Apartment price

    if 7 < nn <= 14:
        sp *= 0.95                  # Discount 5%

    elif nn > 14:
        sp *= 0.7                   # Discount 30%

#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
elif m in ["June", "September"]:
    sp = nn * 75.2
    ap = nn * 68.7

    if nn > 14:
        sp *= 0.8                   # Discount 20%

#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
elif m in ["July", "August"]:
    sp = nn * 76
    ap = nn * 77

#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
if nn > 14:
    ap *= 0.9                        # Discount 10%

# Output
print(f"Apartment: {ap:.2f} lv.")
print(f"Studio: {sp:.2f} lv.")
