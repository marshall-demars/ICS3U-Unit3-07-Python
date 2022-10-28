#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: October 2022
# This program tells a user if they can be dating my grandchild


def main():
    # This function determines if they can date

    # Input
    user_age = input("Enter your age: ")

    # Process and Output
    try:
        user_age_number = int(user_age)
        if user_age_number > 40 or user_age_number < 25:
            print("\nYou are not the right age for my grandchild.")
        else:
            print("\nYou are well suited for my grandchild.")
    except Exception:
        print("\nPlease input a valid number.")

    print("\nDone")


if __name__ == "__main__":
    main()
