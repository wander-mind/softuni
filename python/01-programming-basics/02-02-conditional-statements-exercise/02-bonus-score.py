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
#                        ** Bonus score **
#
#    We are given a whole number - the initial score. On top of it we
# have to add bonus points based on some rules. Write a program that
# calculates the bonus points based ont the initial points (num + bonus)
#
#    Input:
#	1. Initial points
#
#    Bonus points
#	- If num (min - 100] - bonus points +5
#	- If num > 100 - bonus points +20%
#	- If (100 < num < 1000] - bonus points +10%
#
#    Extra bonus points
#	- If num % 2 == 0 - bonus points +1
#	- If num % 10 == 5 - bonus points +2
#
#    Output:
#	1. Bonus points only
#	2. Total score
#

# Input
ip = int(input())	# Initial points
bp = 0			# Bonus points

# Calculation
if ip <= 100:
    bp += 5
elif 100 < ip <= 1000:
    bp += ip * 0.2
elif ip > 1000:
    bp += ip * 0.1

if ip % 2 == 0:
    bp += 1
elif ip % 10 == 5:
    bp += 2

tp = ip + bp		# Total points

# Output
print(bp)
print(tp)
