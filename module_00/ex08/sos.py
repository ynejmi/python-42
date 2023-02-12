
import sys

if len(sys.argv) < 2:
    print("ERROR")
    exit()

# encode the string in morse code


def encode_morse(string):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }
    morse_string = ""
    for char in string:
        if char.upper() in morse_code:
            morse_string += morse_code[char.upper()] + " "
        else:
            morse_string += char + " "
    return morse_string

# check if the argv has alphanumeric characters and whitepsacess only
for char in sys.argv[1]:
    if not char.isalnum() and not char.isspace():
        print("ERROR")
        exit()

# join the argv into a string
string = " ".join(sys.argv[1:])

print(encode_morse(string))