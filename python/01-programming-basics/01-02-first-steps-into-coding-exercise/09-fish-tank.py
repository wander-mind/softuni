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
#                           ** Fish tank **
#
#    For his birth-day Dillan recieved an aquarium in the form of a pa-
# rallelepiped. Write a program that calculates how much water it can
# take, knowing that part of the space is taken up from sand, plants,
# heater, and a pump. 1 liter of water takes up 1 dm^3 of volume.
#
#    Input:
#	1. lenght in cm [10-500]
#	2. width in cm [1--300]
#	3. height in cm [10-200]
#	4. percent ocupied volume [0.000-100.000]
#
#    Output:
#	1. "{Needed liters of water}"
#

# Input
a = int(input())		# Lenght in cm
b = int(input())		# Width in cm
c = int(input())		# Height in cm
perc = float(input())		# Percent ocupied colume

# Calculation
vqcm = a * b * c		# Volume in qubic centimeters
vl = vqcm / 1000		# Volume of liters
os = perc / 100			# Occupied space
nl = vl * (1 - os)		# needed liters of water

# Output
print(f"{nl:.2f}")
