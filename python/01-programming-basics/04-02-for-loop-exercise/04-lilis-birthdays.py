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
age = int(input())              # Lilis age
wmc = float(input())            # Washihng machiene cost
tp = int(input())               # Toy price (for 1)
cash = 0                        # Money she has

# Calculation
for i in range(1, age + 1):
    
    if i % 2 == 0:
        cash += i / 2 * 10 - 1

    else:
        cash += tp              # sells the toys

dif = abs(cash - wmc)           # diference between her cash and wmc

# Output
if cash >= wmc:
    print(f"Yes! {dif:.2f}")

else:
    print(f"No! {dif:.2f}")
