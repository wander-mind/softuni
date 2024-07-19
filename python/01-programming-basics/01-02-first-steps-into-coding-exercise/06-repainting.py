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
#                           ** Repainting **
#
#    Roman wants to paint his livingroom walls and he has hired workers
# to do the job for him. Write a program that calculates the expences
# for the repainting, concidering these prices:
#
#	- protective nylon - 1.50lv. for m^2
#	- paint - 14.50lv. per liter
#	- paint thinner - 5.00lv. per liter
#
#    Roman want to buy extra 10% of paint that is needed, just in case,
# and extra 2 m^2 nylon, and 0.40lv. for plastic bags. The workers get
# payed by the hour, and their price per hour is 30% from the sum of
# all expences for materials.
#
#    Input:
#	1. Nylon [1-100]
#	2. Paint [1-100]
#	3. Thinner [1-30]
#	4. Hours for the workers [1-9]
#
#    Output:
#	1. Print in one line "{the sum of all expences}"
#

# Input
nylon =   int(input())
paint =   int(input())
thinner = int(input())
hours =   int(input())

# Calculation
nc = (nylon + 2) * 1.5		# Nylon cost
pc = paint * 1.1 * 14.5		# Paint cost
tc = thinner * 5		# Thinner cost
bc = 0.40			# Bags cost

tmc = nc + pc + tc + bc 	# Total materials cost
lc = tmc * 0.3 * hours		# Labor cost
total = tmc + lc		# Total expences

# Output
print(f'{total:.2f}')
