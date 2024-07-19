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
#                          ** Shopping **
#
#    Peter wants to buy N amount of videocards, M amount of processors,
# and P amount of RAMs. If the amount of videocards is greater than the
# amount of proccessors, he gets 15% off of the final price.
#
#    The prices:
#       - Videocard - 250lv
#       - processor - 35% of the price payed for the videocards (1 proc)
#       - RAM - 10% of the price payed for the videocards (1 stick)
#
#    Write a program that how much Peters purchase will cost, and if his
# budget covers it.
#
#    Input:
#       1. Peters budget (R)            [1.0 - 100000.0]
#       2. Number of videocards         [1 - 100]
#       3. Number of proccessors        [1 - 100]
#       4. Amount of RAM sticks         [1 - 100]
#
#    Output:
#       1. If his budget fits the price:
#           - "You have {money left} leva left!"
#       2. If his budget in not enough:
#           - "Not enough money! You need {money needed} leva more!"
#
#    The money has to be printed to the second decimal [0.00].
#

# Input
B = float(input())          # Budget
N = int(input())            # Videocards
M = int(input())            # Proccessors
P = int(input())            # RAM

# Calculation
vp = N * 250                # Videocards price
pp = M * vp * 0.35          # Proccessor price
rp = P * vp * 0.1           # RAM price
tp = vp + pp + rp           # Total price

if N > M:
    tp *= 0.85              # 15% off total price

# Output
if B >= tp:
    ml = B - tp             # Money left
    print(f"You have {ml:.2f} leva left!")
else:
    mn = tp - B             # Money needed
    print(f"Not enough money! You need {mn:.2f} leva more!")
