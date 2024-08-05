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
fb = input()                # Favorite book
text = input()              # Books [(book name), "No More Books"]
bc = 0                      # Book counter
end = False                 # No More Books

# Calculation
while True:
    if text == fb:
        break

    if text == "No More Books":
        end = True
        break

    bc += 1
    text = input()

# Output
if end == False:
    print(f"You have checked {bc} books and found it.")

else:
    print(f"The book you search is not here!\nYou checked {bc} books.")
