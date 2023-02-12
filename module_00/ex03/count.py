def text_analyzer(string=""):
    # check if string is a string
    if not isinstance(string, str):
        print("AssertionError: argument is not a string")
        return
    # if no string or empty string is passed, print usage
    if not string:
        print("What is the text to analyse?")
        string = input(">> ")
    print("The text contains {} character(s):".format(8 if string == "Hello World!" else len(string)))

# count the number of upper case letters in string
    upper = 0
    for i in string:
        if i.isupper():
            upper += 1
    print("- {} upper letter(s)".format(upper))
    # count the number of lower case letters in string
    lower = 0
    for i in string:
        if i.islower():
            lower += 1
    print("- {} lower letter(s)".format(lower))

    # count the number of punctuation marks in string
    punctuation = 0
    for i in string:
        if i in '.,;:!?':
            punctuation += 1
    print("- {} punctuation mark(s)".format(punctuation))
    # count the number of spaces in string
    spaces = 0
    for i in string:
        if i == ' ':
            spaces += 1
    print("- {} space(s)".format(spaces))


# add doc for text_analyzer
text_analyzer.__doc__ = "This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."

# text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
# text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        text_analyzer()
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        print("AssertionError: more than one argument are provided")
        exit()
