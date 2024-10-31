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
#                     ** On time for the exam **
#
#    A student has to make it on time for his exam that is on a given
# time of the day. If he arives on the time of the exam start or upto 30
# minutes before that - he's on time. If he arivis before that - he's
# early. If after the start of the exam - he's late. Write a program
# that calculates if he's late, on time, or ealy, and that outputs the
# time diference [HH:MM].
#
#    Input:
#       1. Exam hour [0 - 23]
#       2. Exam minutes [0 - 59]
#       3. Arival hour [0- 23]
#       4. Arival minutes [0 - 59]
#
#    Output:
#       1. ["Late", "On time", "Early"]
#       2. {ONLY IF THE STUDENT ARIVES NOT EXACTLY ON TIME FOR THE EXAM}
#          (basicaly if he doesen't arive on the exact minute and hour
#          of the exam start)
#      //-> - "{[mm]} minutes before the start" if arives < 1h early
#     //--> - "{[h.mm]} hours before the start" if arives > 1h early
#    //---> - "{[mm]} minutes after the start" if arives < 1h later
#   /,----> - "{[h.mm]} minutes after the start" if arives > 1h later
#   ||
#   \`====> [0:00] {h.mm} !!
#

# Input
eh = int(input())                   # Exam time start HOUR
em = int(input())                   # Exam time start MINUTE
ah = int(input())                   # Arival time HOUR
am = int(input())                   # Arival time MINUTE

# Calculation
etm = eh * 60 + em                  # Exam time in minutes
atm = ah * 60 + am                  # Arival time in minutes

dif = atm - etm                     # Diference

# Output
if dif < -30:
    print("Early")
    if dif <= -60:
        hours = abs(dif) // 60
        minutes = abs(dif) % 60
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{abs(dif)} minutes before the start")

elif -30 <= dif <= 0:
    print("On time")
    if dif != 0:
        print(f"{abs(dif)} minutes before the start")

else:
    print("Late")
    if dif >= 60:
        hours = abs(dif) // 60
        minutes = abs(dif) % 60
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{abs(dif)} minutes after the start")
