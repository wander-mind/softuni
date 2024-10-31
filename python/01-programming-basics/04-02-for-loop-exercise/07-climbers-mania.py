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

# Input
ng = int(input())               # Number of climbing groups

mu = 0          # Musala
mo = 0          # Monblan
ki = 0          # Kilimanjaro
k2 = 0          # K2
ev = 0          # Everest

# Calculation
for i in range(0, ng):
    np = int(input())           # Number of people in the group

    if np <= 5:
        mu += np

    elif 6 <= np <= 12:
        mo += np

    elif 13 <= np <= 25:
        ki += np

    elif 26 <= np <= 40:
        k2 += np

    else:
        ev += np

tp = mu + mo + ki + k2 + ev     # Total people climbing

mup = mu / tp * 100             # Musala      people in percents
mop = mo / tp * 100             # Monblan     people in percents
kip = ki / tp * 100             # Kilimanjaro people in percents
k2p = k2 / tp * 100             # K2          people in percents
evp = ev / tp * 100             # Everest     people in percents

# Output
print(f"{mup:.2f}%")
print(f"{mop:.2f}%")
print(f"{kip:.2f}%")
print(f"{k2p:.2f}%")
print(f"{evp:.2f}%")
