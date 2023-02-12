# This is an interactive guessing game!
# You have to enter a number between 1 and 99 to find out the secret number.
# Type 'exit' to end the game.
# Good luck!
# What's your guess between 1 and 99?
# >> 54
# Too high!
# What's your guess between 1 and 99?
# >> 34
# Too low!
# What's your guess between 1 and 99?
# >> 45
# Too high!
# What's your guess between 1 and 99?
# >> A
# That's not a number.
# What's your guess between 1 and 99?
# >> 43
# Congratulations, you've got it!
# You won in 5 attempts!

print ( "This is an interactive guessing game!" )
print ( "You have to enter a number between 1 and 99 to find out the secret number." )
print ( "Type 'exit' to end the game." )
print ( "Good luck!\n" )

import random

number = random.randint(1, 99)

count = 1
guess = 0

while guess != number:
    guess = 0
    print ( "What's your guess between 1 and 99?" )
    while not guess:
        guess = input(">> ")

    if guess == "exit":
        print ( "Goodbye!" )
        exit()

    try:
        guess = int(guess)
        if guess > number:
            print ( "Too high!" )
        elif guess < number:
            print ( "Too low!" )
        count += 1
    except:
        print ( "That's not a number." )

if number == 42:
    print ( "The answer to the ultimate question of life, the universe and everything is 42." )

if count == 1:
    print ( "Congratulations! You got it on your first try" )
else:
    print ( "You won in" , count , "attempts!" )