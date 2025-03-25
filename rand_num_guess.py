#!/usr/bin/env python3


# Created By: Amara Tie


# Date: March 21, 2025


# In this code the user will guess the randomly generated number.
import random




def main():
    # Generate the random number
    random_number = random.randint(2, 57)

    # Get the user's guess
    user_guess = int(input("Enter a number between 2 and 57: "))
    print("")

    # If the user guessed correctly or incorrect
    if user_guess == random_number:
        print("The number was {} you are correct!".format(random_number))
    else:
        print("The number was {} you are incorrect".format(random_number))


if __name__ == "__main__":
    main()
