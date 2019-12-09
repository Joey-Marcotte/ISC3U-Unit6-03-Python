#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: Dec 2019
# This program uses a list as a parameter

import random


def lowest_value(list_of_numbers):
    # this functions finds the lowest number in the list

    lowest_number = list_of_numbers[0]

    for a_single_number_from_list in list_of_numbers:
        if a_single_number_from_list < lowest_number:
            lowest_number = a_single_number_from_list

    return lowest_number


def main():
    # this function uses a list

    random_numbers = []
    lowest = 0

    # input
    number_of_numbers = input("How mamy numbers would you like to generate? ")

    try:
        numbers = int(number_of_numbers)

        print("The numbers are ")
        for loop_counter in range(0, numbers):
            a_single_number = random.randint(0, 10)
            random_numbers.append(a_single_number)
            print("{0}, ".format(a_single_number), end="")
        print("")

        lowest = lowest_value(random_numbers)

        print("The lowest number is: {0} ".format(lowest))

    except(ValueError):
        print("Invalid input")


if __name__ == "__main__":
    main()
