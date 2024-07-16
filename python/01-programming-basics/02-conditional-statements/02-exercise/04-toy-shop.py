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
#                          ** Toy shop **
#
#    Jane own a toy shop, nad she gets a big order, which she has to
# fulfil. With the money she is going to make, she want to go on a vaca-
# tion.
#
#    Toys prices:
#       - Puzzle: 2.60lv.
#       - Talking doll: 3lv.
#       - Teddy bear: 4.10lv.
#       - Minion: 8.20lv.
#       - Truck: 2lv.
#
#    If the ordered toys are 50 or more, the store gives a 25% discount.
# From the money she made, Jane has to pay 10% for the store's rent.
# Calculate if she will make enough money for the vacation.
#
#    Input:
#       1. Vacation price (R)       [1.00 - 10000.00]
#       2. Number of puzzles        [0 - 1000]
#       3. Number of talking dolls  [0 - 1000]
#       4. Number of teddy bears    [0 0 1000]
#       5. Number of minions        [0 - 1000]
#       6. Number of trucks         [0 - 1000]
#
#    Output:
#       1. If the money is enough for thr vacation:
#           - print "Yes! {money left} lv left."
#       2. If the money is NOT enough for the vacation:
#           - print "Not enough money! {money needed} lv needed."
#
#    The result has to be printed to the second decimal.
#

# Input
vp = float(input())     # Vacation price
pc = int(input())       # Puzzle count
dc = int(input())       # Doll count
tbc = int(input())      # Teddy bear count
mc = int(input())       # Minion count
tc = int(input())       # Truck count

# Calculation
tt = pc + dc + tbc + mc + tc                            # Total toys
tm = pc * 2.6 + dc * 3 + tbc * 4.1 + mc * 8.2 + tc * 2  # Total money

if tt >= 50:
    tm *= 0.75          # 25% discount

tm *= 0.9               # 10% rent
ml = tm - vp            # Money left

# Output
if ml >= 0:
    print(f"Yes! {ml:.2f} lv left.")
else:
    print(f"Not enough money! {abs(ml):.2f} lv needed.")