
import sys

try:
    if len(sys.argv) != 3:
        raise ValueError

    string = sys.argv[1]
    n = int(sys.argv[2])

    words = string.split()

    # remove punctuation characters
    for i in range(len(words)):
        words[i] = ''.join(e for e in words[i] if e.isalnum())

    # remove words with less than n characters
    words = [word for word in words if len(word) > n]

    print(words)
except:
    print("ERROR")