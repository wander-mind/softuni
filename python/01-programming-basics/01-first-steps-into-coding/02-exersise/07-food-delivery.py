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
#                        ** Food delivery **
#
#    Write a program that calculates how much it will cost for a group
# of people to order food for home.
#    
#    Restaurant menu:
#	- Chicken menu - 10.35lv.
#	- Fish menu - 12.40lv.
#	- Pork menu - 8.15lv.
#
#    The group will also order desssert, which costs 20% of the order
# price, and the delivery costs 2.50lv. on top of all costs.
#
#    Input:
#	1. Amount of chicken menus [0-99]
#	2. Amount of fish menus [0-99]
#	3. Amount of pork menus [0-99]
#
#    Output:
#	1. Print in one line "{the total cost}"
#

# Input
chicken = int(input())
fish = int(input())
pork = int(input())

# Calculation
cp = chicken * 10.35	# Chicken menus price
fp = fish * 12.40	# Fish menus price
pp = pork * 8.15	# Pork menus price

tmp = cp + fp + pp	# Total menus price
dp = tmp * 0.2		# Desert price
top = tmp + dp + 2.5	# Total order price (+ 2.50lv. for delivery)

# Output
print(f'{top:.2f}')
