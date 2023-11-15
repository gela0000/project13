"""
File: class_reviews.py
Name: Angela
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = "-1"  # This str controls when the program stops.


def main():
    """
    TODO: This program finds the highest score, the lowest score, and the avg score of classes SC001 and SC101.
    """
    count_001 = 0  # counts records the number of scores of SC001
    count_101 = 0  # counts records the number of scores of SC101

    total_001 = 0
    max_001 = 0
    min_001 = 0

    total_101 = 0
    max_101 = 0
    min_101 = 0

    c = upper(input("Which class? "))
    if c == EXIT:  # check if any scores were entered
        print("No class score were entered.")
    else:
        while True:
            if c == EXIT:
                break
            else:
                score = int(input("Score: "))
                if c == "SC001":
                    count_001 += 1
                    total_001 += score
                    if score > max_001 or max_001 == 0:  # When new score is maximum or max_001 == initial value
                        max_001 = score
                    if score < min_001 or min_001 == 0:  # When new score is minimum or min_001 == initial value
                        min_001 = score
                if c == "SC101":
                    count_101 += 1
                    total_101 += score
                    if score > max_101 or max_101 == 0:  # When new score is maximum or max_101 == initial value
                        max_101 = score
                    if score < min_101 or min_101 == 0:  # When new score is minimum or min_101 == initial value
                        min_101 = score
            c = upper(input("Which class? "))

        print("=============SC001=============")
        if count_001 == 0:  # check if any scores were entered for sc001
            print("No score for SC001")
        else:
            print("Max (001): " + str(max_001))
            print("Min (001): " + str(min_001))
            print("Avg (001): " + str(total_001 / count_001))

        print("=============SC101=============")
        if count_101 == 0:  # check if any scores were entered for sc101
            print("No score for SC101")
        else:
            print("Max (101): " + str(max_101))
            print("Min (101): " + str(min_101))
            print("Avg (101): " + str(total_101 / count_101))


def upper(c):
    """
    :param: original string
    :return: capitalized string
    """
    upper_c = ""
    for i in range(len(c)):
        ch = c[i]
        if ch.islower():
            upper_c += ch.upper()
        else:
            upper_c += ch
    return upper_c


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
