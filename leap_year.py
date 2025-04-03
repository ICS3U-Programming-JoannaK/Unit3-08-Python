#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 3, 2025
# This program casts a string to an integer, and 
# lets the user know if the year they wrote was 
# a leap year or not a leap year

def main():
    # get user's input
    year_string = input("Enter the year: ")

    # CAST the string into an integer
    try:
        year_integer = int(year_string)
        if year_integer % 4 == 0:
            if year_integer % 100 == 0:
                if year_integer % 400 == 0:
                    print("{} is a leap year !".format(year_integer))
                else:
                    print("{} is not a leap year".format(year_integer))
            else:
                print("{} is a leap year".format(year_integer))
        else:
            print("{} is not a leap year".format(year_integer))
    except Exception:
        print("{} is not valid year".format(year_string))

if __name__ == "__main__":
    main()