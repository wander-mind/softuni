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
#                         ** Area of figures **
#
#    Write a program in which the user enters the type and size of a ge-
# ometric figure, and calculates its area.
#
#    4 types of figures:
#	- square
#	- rectangle
#	- circle
#	- triangle
#
#    - If the figure is a square, the input is:
#	1. The lenght of one of its sides (R). 
#
#    - If the figure is a rectangle, the inputs are:
#	1. The lenght of one of its sides (R).
#	2. The lenght of one of its non-oposite sides (R).
#
#    - If the figure is a circle, the input is:
#	1. The radius of the circle (R).
#
#    - If the figure is a triangle, the inputs are:
#	1. The lenght of one of its sides (R).
#	2. The lenght of that sides height (R).
#
#    Print the result untill the third decimal.
#

ft = input()		# Figure type

if ft == "square":
    a = float(input())	# Side lenght
    area = a ** 2

elif ft == "Rectangle":
    a = float(input())	# Width
    b = float(input())	# height
    area = a * b

elif ft == "circle":
    r = float(input())	# Radius
    import math		# Needed for Pi
    area = math.pi * r ** 2

elif ft == "triangle":
    a = float(input())	# Side lenght
    ha = float(input())	# Height lenght
    area = a * ha / 2

print(f"{area:.3f}")
