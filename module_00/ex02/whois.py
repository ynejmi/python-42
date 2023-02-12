import sys
# if no arguments are passed, print usage
if len(sys.argv) == 1:
    print("usage: python3 whois.py <number>")
    exit()

# f is not a number error or multiple arguments error
try:
    number = int(sys.argv[1])
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument are provided")
        exit()
except ValueError:
    print("AssertionError: argument is not an integer")
    exit()

# is number odd or even?

if number == 0:
    print("I'm Zero.")
elif number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
