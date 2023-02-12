import sys
# If no argument are provided, do nothing or print an usage
if len(sys.argv) == 1:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("python operations.py 10 3")
    exit()

# If more or less than two argument are provided or if either of the argument is not an integer, print an error message
if len(sys.argv) > 3:
    print("AssertionError: too many arguments")
    exit()
elif len(sys.argv) < 3:
    print("AssertionError: not enough arguments")
    exit()
elif not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("AssertionError: only integers")
    exit()

print("Sum: {}".format(int(sys.argv[1]) + int(sys.argv[2])))
print("Difference: {}".format(int(sys.argv[1]) - int(sys.argv[2])))
print("Product: {}".format(int(sys.argv[1]) * int(sys.argv[2])))
if int(sys.argv[2]) == 0:
    print("Quotient: ERROR (div by zero)")
    print("Remainder: ERROR (modulo by zero)")
else:
    print("Quotient: {}".format(int(sys.argv[1]) / int(sys.argv[2])))
    print("Remainder: {}".format(int(sys.argv[1]) % int(sys.argv[2])))
