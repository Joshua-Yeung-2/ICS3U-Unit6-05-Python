# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on October 2021
# This program is to calculate the average of the user input


def average(number):
    total = 0
    for loop_counter in number:
        total += loop_counter
    average_number = total / len(number)

    return average_number


def main():
    # this function is to calculate the average of random number
    print("Please enter 1 mark at a time. Enter -1 to end.")
    number = []

    while True:
        # input
        marks = input("What is your mark? (as %): ")
        # process
        try:
            marks_int = int(marks)
            number.append(marks_int)
            if marks_int == -1:
                break
        except Exception:
            print("sorry, this is not a valid number")
            print("please try again")
    number.pop()  # remove the -1 that was added
    # call function
    average_number_2 = average(number)
    print("")
    print("The average is {0} ".format(average_number_2))

    print("\nDone")


if __name__ == "__main__":
    main()
