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
#                   ** Basketball equipment **
#
#    Jessy desides she wants to train basketball, but she needs equip-
# ment. Write a program which calculates what expences Jessy will have
# if she starts training, knowing how much the membership costs for 1
# year.
#
#    Needed equipment:
#	1. sneekers - the price is 40% less than the yearly membership
#	2. clothes - 20% cheaper than the sneakers
#	3. ball - 1/4-th the price of the clothes
#	4. accessories - 1/5-th the price of the ball
#
#    Input:
#	1. Yearly membership cost [0-9999]
#
#    Output:
#	1. "{Yearly total cost}"
#

# Input
mp = int(input())	# Membership cost

# Calculation
sp = mp * 0.6		# Sneakers price 60% of the mp (-40%)
cp = sp * 0.8		# Clothes price 80% of the sp (-20%)
bp = cp / 4		# Ball price 25% of the cp (-75%)
ac = bp / 5		# Accessories price 20% of the bp (-80%)

total = mp + sp + cp + bp + ac	# Total price

# Output
print(f"{total:.2f}")
