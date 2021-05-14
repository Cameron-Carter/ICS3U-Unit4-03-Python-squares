#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program squares ascending integers
import string


def main():
    # This function squares numbers

    # Input
    input_as_string = str(input("Enter an integer >= 0: "))

    # Process and Output
    try:
        input_as_integer = int(input_as_string)
        if input_as_integer >= 0:
            for loop_counter in range(input_as_integer + 1):
                product = loop_counter ** 2
                print("{0}² = {1}".format(loop_counter, product))
        else:
            print("\n{} is not a positive number".format(input_as_string))
    except Exception:
        print("\n{} is not a positive integer".format(input_as_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
