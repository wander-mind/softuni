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

# ** Stream of characters from a string **

# Input
text = input()              # The text we will print letter by letter

# Calculation & Output
for i in range(0, len(text)):
    print(text[i])