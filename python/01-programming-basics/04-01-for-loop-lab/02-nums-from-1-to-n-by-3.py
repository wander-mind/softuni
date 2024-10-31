#██╗    ██╗ █████╗ ███╗   ██╗██████╗ ███████╗██████╗
#██║    ██║██╔══██╗████╗  ██║██╔══██╗██╔════╝██╔══██╗
#██║ █╗ ██║███████║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
#██║███╗██║██╔══██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
#╚███╔███╔╝██║  ██║██║ ╚████║██████╔╝███████╗██║  ██║
# ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝

#███╗   ███╗██╗███╗   ██╗██████╗    E-Mail: w.m@tuta.com
#████╗ ████║██║████╗  ██║██╔══██╗
#██╔████╔██║██║██╔██╗ ██║██║  ██║   GitHub: github.com/
#██║╚██╔╝██║██║██║╚██╗██║██║  ██║              wander-mind
#██║ ╚═╝ ██║██║██║ ╚████║██████╔╝
#╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝      Site: wandermind.xyz

#   ** Numbers from 1 to N in steps of 3 **

#   Write a program that prints the numbers from 1 to the number inputed by the user, in steps of 3 (1, 4, 7...).

#   Input:
#       1. Number to count to (whole number).

# Input
n = int(input())

# Calculation and Output
for i in range(1, n + 1, 3):
    print(i)
