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
#                         ** World swimming **
#                             ** record **
#
#    Ivan decides to brake the world record for swimming long distances.
# In the console we have to input the current record (in seconds), which
# Ivan has to beat, the distance (in meters), which he has to swim, and
# the time (in seconds) that he is able to swim for 1 meter. Write a
# program which calculates if he was successful, when you have in mind
# that the water drag slows him down with 12.5s/15m.
#
#    Input:
#	1. The world record in seconds (R)
#	2. The distance in meters (R)
#	3. The time in which he swims 1 meter (R)
#
#    Output:
#	1. If Ivan beats the world record:
#		- "Yes, he succeeded! The new world record is +
#		  {his time} seconds."
#	2. If not:
#		- "No, he failed! He was {needed time} seconds slower."
#
#    The result has to be rounded to the second decimal.
#

# Input
wr = float(input())		# World record (in seconds)
dm = float(input())		# Distance in meters
tpm = float(input())		# Time per meter (for Ivan)

# Calculation
multiplier = dm // 15		# How many times water drags him 12.5s
dt = multiplier * 12.5		# Drag time (in seconds)
ss = (dm * tpm) + dt		# Swim seconds

# Output
if ss < wr:
    print(f"Yes, he succeeded! The new record is {ss:.2f} seconds.")
else:
    tn = ss - wr		# Time needed to beat the record
    print(f"No, he failed! He was {tn:.2f} seconds slower.")
