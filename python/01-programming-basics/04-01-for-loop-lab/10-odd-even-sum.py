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

# Write a program that reads N amount of numbers, and checks if the sum of the even numbers is equal to the sum of the odd numbers.

# Input
n = int(input())            # Amount of numbers to input and compare
counter = 1
total1 = 0
total2 = 0

# Calculation
for i in range(0, n):
    
    if counter % 2 == 0:
        total1 += int(input())
    else:
        total2 += int(input())

    counter += 1

# Output
if total1 == total2:
    print(f"Yes\nSum = {total1}")

else:
    dif = abs(total1 - total2)
    print(f"No\nDiff = {dif}")
