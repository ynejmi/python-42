import sys
# if no arguments are passed, print usage
if len(sys.argv) == 1:
    print("usage: python3 exec.py <whatever>")
    exit()

output = ' '.join(sys.argv[1:])

output = output[::-1]

output = output.swapcase()

print(output)

# print(sys.argv[1:7:2])
