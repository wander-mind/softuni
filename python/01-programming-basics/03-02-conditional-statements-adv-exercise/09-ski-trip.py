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
#                            ** Ski trip **
#
#    Jimmy decides to take some vacation days to go skiing, but before
# he goes he has to reserve a hotel room, and also calculate how much it
# cost him. These are the 3 types of rooms avalable:
#
#       - "room for one person"     - 18lv per night
#       - "apartment"               - 25lv per night
#       - president apartment"      - 35lv per night
#
#    Based on the number of days he is going to stay (e.g. 11 days = 10
# nights), and the type of room, he can use diferent types of discounts.
#
#  /------------------------------------------------------------------\
# /    Type of room     |  days < 10  | 10 < days <= 15 |  days > 15   \
# |~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~|
# |  Room for 1 person  | No discount |   No Discount   | No Discount  |
# |      Apartment      |     30%     |       35%       |      50%     |
# \ President apartment |     10%     |       15%       |      20%     /
#  \------------------------------------------------------------------/
#
#    After his stay, Jimmys rating for the hotel may be positive or ne-
# gative. If his rating is positive he pays an extra 25% on top of the
# discounted price. If negative - he pays 10% less.
#
#    Input:
#       1. Days at the hotel [0 - 365]
#       2. Type of room ["room for one person", "apartment", "president
#                                                            apartment"]
#       3. Rating ["positive", "negative"]
#
#    Output:
#       1. Price for the hotel (R) [0.00]
#

# Input
d = int(input())                    # Days stay
tr = input()                        # Type of room
r = input()                         # Rating

# Calculation
n = d -1                            # Nights = days - 1

if tr == 'room for one person':
    rp = n * 18                     # Room price

#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
elif tr == 'apartment':
    rp = n * 25

    if 10 > d:
        rp *= 0.7                   # Discount 30%
    elif 10 <= d <= 15:
        rp *= 0.65                  # Discount 35%
    elif d > 15:
        rp *= 0.5                   # Discount 50%

#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
elif tr == 'president apartment':
    rp = n * 35

    if 10 > d:
        rp *= 0.9                   # Discount 10%
    elif 10 <= d <= 15:
        rp *= 0.85                  # Discount 15%
    elif d > 15:
        rp *= 0.8                   # Discount 20%

#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
if r == "positive":
    rp *= 0.75                      # Discount 25% extra
elif r == "negative":
    rp *= 1.1                       # 10% extra charge

# Output
print(f"{rp:.2f}")
