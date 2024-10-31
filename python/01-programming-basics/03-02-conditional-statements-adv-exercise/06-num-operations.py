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
#                  ** Operations between numbers **
#
#    Write a program that reads two whole numbers N1 and N2, and an ope-
# rator, with which to do a mathematical operation.
#
#    Operations:
#       - Add       (-)
#       - Subtract  (+)
#       - Multiply  (*)
#       - Divide    (/)
#       - Modal     (%)
#
#    When adding, subtracting, and multiplying we have to print if the
# result is even or odd, when dividing - the result, and when modal de-
# vidilng - the fraction left after division. We have to keep in mind
# that it's imposible to divide by 0, so in that case we have to print a
# special message.
#
#    Input:
#       1. N1 (whole number)
#       2. N2 (whole number)
#       3. Operator ["+", "-", "*", "/", "%"]
#
#    Output:
#       1. If the operator is "+", "-", "*":
#           - print "{N1} {operator} {N2} = {result} - {[even, odd]}"
#          If the operator is "/":
#           - print "{N1} / {N2} = {result [0.00]}"
#          If the operator is "%":
#           - print "{N1} % {N2} = {fraction left}"
#          If N2 is 0 and the operator is "/" or "%":
#           - print "Cannot divide {N1} by zero"
#

# Input
n1 = int(input())                   # First number
n2 = int(input())                   # Second number
o = input()                         # Operator

# Calculation & output
if n2 == 0 and o in ["/", "%"]:
    print(f"Cannot divide {n1} by zero")

else:

    if o in ["+", "-", "*"]:

        if o == "+":
            res = n1 + n2           # Result
        elif o == "-":
            res = n1 - n2
        else:
            res = n1 * n2

        if res % 2 == 0:
            eo = "even"             # Even or odd
        else:
            eo = "odd"

        print(f"{n1} {o} {n2} = {res} - {eo}")

    elif o == "/":
        res = n1 / n2
        print(f"{n1} / {n2} = {res:.2f}")

    elif o == "%":
        res = n1 % n2
        print(f"{n1} % {n2} = {res}")

