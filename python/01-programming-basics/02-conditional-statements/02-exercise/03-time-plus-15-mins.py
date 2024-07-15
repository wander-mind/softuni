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
#                        ** Time + 15 minutes **
#
#    Write a program that reads from the console, entered by the user,
# hours and minutes in 24-hours format, and calculates what the time
# will be in 15 minutes time. The result has to be printed in the format
# "hours:minutes". The hours are always [0 - 23], and the minutes [0 -
# 59]. The hours can be printed with 1 or 2 digits, but the minutes al-
# ways have to be 2 digits, with a 0 in front when needed.
#
#   Input:
#	1. hours [0-23]
#	2. Minutes [0-59]
#
#   Output:
#	1. time + 15 minutes [0:00 - 23:59]
#

# Input
h = int(input())	# Hours
m = int(input())	# Minutes

# Calculation
tm = h * 60 + m + 15	# Total minutes
nh = tm // 60		# New Hours
nm = tm % 60		# New minutes

# Output
print(f"{nh % 24:2d}:{nm:02d}")
