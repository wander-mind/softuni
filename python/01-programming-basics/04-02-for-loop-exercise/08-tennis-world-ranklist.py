#██╗    ██╗ █████╗ ███╗   ██╗██████╗ ███████╗██████╗
#██║    ██║██╔══██╗████╗  ██║██╔══██╗██╔════╝██╔══██╗
#██║ █╗ ██║███████║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
#██║███╗██║██╔══██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
#╚███╔███╔╝██║  ██║██║ ╚████║██████╔╝███████╗██║  ██║
# ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
#███╗   ███╗██╗███╗   ██╗██████╗ E-Mail: w.m@tuta.com
#████╗ ████║██║████╗  ██║██╔══██╗
#██╔████╔██║██║██╔██╗ ██║██║  ██║ GitHub: github.com/
#██║╚██╔╝██║██║██║╚██╗██║██║  ██║         wander-mind
#██║ ╚═╝ ██║██║██║ ╚████║██████╔╝
#╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ Site: wandermind.xyz

import math

# Input
nt = int(input())           # Number of tournaments
sp = int(input())           # Starting points for the tournament

pw = 0          # Points won
nwg = 0         # Number of winning games

# Calculation
for i in range(0, nt):
    te = input()            # Tournament end [W, F, SF]

    if te == "W":
        pw += 2000
        nwg += 1

    elif te == "F":
        pw += 1200

    elif te == "SF":
        pw += 720

pwg = nwg / nt * 100        # Percent winning games
average = pw / nt           # Average point won in the tournaments

avg = math.floor(average)   # Average rounded

# Output
print(f"Final points: {sp + pw}")
print(f"Average points: {math.floor(average)}")
print(f"{pwg:.2f}%")
