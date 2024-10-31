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
#                        ** Godzilla VS Kong **
#
#    The filming for the movie "Godzilla VS Kong" begin! The screenwri-
# ter is asking us to write a program that calculates if the projected
# budget will be enough for filming. For the pictures they will need a
# specific number of statists, costumes for them, & decor.
#
#    We know that:
#	- The decor is worth 10% of the budget.
#	- When the statists > 150 - 10% discount for the costumes.
#
#    Input:
#	1. Film budget (R)		[1.00 - 1000000.00]
#	2. Statist number		[1 - 500]
#	3. Costume cost per person (R)	[1.00 - 1000.00]
#
#    Output:
#	1. If the money for the decor > budget:
#		- "Not enough money!"
#		- "Wingard needs {needed $} leva more."
#	2. If the money for the decor <= budget:
#		- "Action!"
#		- "Wingard strats filming with {$ left} leva left."
#
#    Result has to be printed to the second decimal [0.00]
#

# Input
fb = float(input())		# Film budget
sn = int(input())		# Statist number
cc = float(input())		# Costume cost

# Calculation
dp = fb * 0.1			# Decor price
cp = sn * cc			# Costume price

if sn > 150:
    cp *= 0.9			# Clothing price -10%

tc = dp + cp			# Total cost

# Output
if tc > fb:
    nm = tc - fb		# Needed money
    print("Not enough money!")
    print(f"Wingard needs {nm:.2f} leva more.")
else:
    ml = fb - tc		# Money left
    print("Action!")
    print(f"Wingard starts filming with {ml:.2f} leva left.")
