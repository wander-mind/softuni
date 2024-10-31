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
#                        ** Summer outfit **
#
#    Write a program that, based on the time of day and temperature, he-
# lps Victorchose what clothes to wear. He has diferent outfits he wants
# to wear based on the diferent conditions.
#
#  ____________________________________________________________________
# / time of |                   |                   |                  \
# | day /   |      Morning      |     Afternoon     |      Evening     |
# | degrees |                   |                   |                  |
# |---------|-------------------|-------------------|------------------|
# |  10 <=  |  Outfit = Sweat-  |  Outfit = Shirt,  |  Outfit = Shirt, |
# | degrees |  shirt, Shoes =   | Shoes = Moccasins | Shoes = moccasins|
# |  <= 18  |     Sneakers      |                   |                  |
# |---------|-------------------|-------------------|------------------|
# |  18 <   |  Outfit = shirt,  | Outfit = T-Shirt, | Outfit = Shirt,  |
# | degrees | Shoes = Moccasins |  Shoes = Sandals  | Shoes = Moccasins|
# |  <= 24  |                   |                   |                  |
# |---------|-------------------|-------------------|------------------|
# |         | Outfit = T-Shirt, |   Outfit = Swim   |  Outfit = Shirt, |
# | degrees |  Shoes = Sandals  |   Suit, Shoes =   |  Shoes = Mocca-  |
# |  => 25  |                   |      Barefoot     |       sins       |
# \_________|___________________|___________________|__________________/
#
#    Input:
#       1. Degrees (whole number)
#       2. Time of day [Morning, Afternoon, Evening]
#
#    Output:
#       1. "It's {degrees} degrees, get your {outfit} and {shoes}."
#

# Input
deg = int(input())              # Degrees outside
td = input()                    # Time of day

# Calculation
o1 = "Sweatshirt"               # Outfit 1
o2 = "Shirt"                    # Outfit 2
o3 = "T-Shirt"                  # Outfit 3
o4 = "Swim Suit"                # Outfit 4

s1 = "Sneakers"                 # Shoes 1
s2 = "Moccasins"                # Shoes 2
s3 = "Sandals"                  # Shoes 3
s4 = "Barefoot"                 # Shoes 4

if 10 <= deg <= 18:
    if td == 'Morning':
        outfit = o1
        shoes = s1
    elif td == 'Afternoon':
        outfit = o2
        shoes = s2
    elif td == 'Evening':
        outfit = o2
        shoes = s2

elif 18 <= deg <= 24:
    if td == 'Morning':
        outfit = o2
        shoes = s2
    elif td == 'Afternoon':
        outfit = o3
        shoes = s3
    elif td == 'Evening':
        outfit = o2
        shoes = s2

elif deg >= 25:
    if td == 'Morning':
        outfit = o3
        shoes = s3
    elif td == 'Afternoon':
        outfit = o4
        shoes = s4
    elif td == 'Evening':
        outfit = o2
        shoes = s2

# Output
print(f"It's {deg} degrees, get your {outfit} and {shoes}.")
