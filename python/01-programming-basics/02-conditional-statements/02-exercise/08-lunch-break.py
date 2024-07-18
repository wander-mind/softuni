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
#                         ** Lunch break **
#
#    During his lunch break, Chuck wants to watch an episode from his
# favorite TV-show. Write a program that will calculate if he will have
# enough time to watvh an episode. During the lunch break he separates
# his time for lunch, leasure, and time remaining for watching.
#
#    - The time for lunch will be 1/8 of brake time.
#    - Leasure time will be 1/4 of brake time.
#
#    Input:
#       1. Name of the TV-Show [text]
#       2. Continuation for an episode in minutes [10 - 90]
#       3. Continuation for the break time in minutes [10 - 120]
#
#    Output:
#       1. If the time is enough to watch an episode:
#           - "You have enough time to watch {name} and left with +
#           {time left} minutes free time."
#       2. If the time isn't enough:
#           - "You don't have enough time to watch {name}, you need +
#           {time needed} more minutes.
#
#    Round the time to the closest bigger integer."
#

import math                     # For the math functions

# Input
name = input()
cem = int(input())                  # Continuation of episode in minutes
cbm = int(input())                  # Continuation of break in minutes

# Calculation
lt1 = cbm * 0.125                   # Lunch time (1/8)
lt2 = cbm * 0.25                    # Leasure time (1/4)

tl = cbm - lt1 - lt2                # Time left for episode
tlaw = math.ceil(tl - cem)          # Time left after watching
tnfw = math.ceil(cem - tl)          # Time needed to watch

#    "abs()" on (tl - cem) won't work for both cases in "# Output", be-
# cause math.ceil() on a negative number in the "else" case will actual-
# ly give us the lower number when we absolute the value.

# Output
if tl >= cem:
    print(f"You have enough time to watch {name} and left with {tlaw} " +
          "minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {tnfw}"+
          " more minutes.")
