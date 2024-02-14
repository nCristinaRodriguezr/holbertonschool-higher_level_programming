#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    for i in range(len(roman_string)):
        if i+1 < len(roman_string):
            if (roman_string[i] == "C" and
                roman_string[i+1] != "D" and
                    roman_string[i+1] != "M"):
                number = number + 100
            elif (roman_string[i] == "C" and
                  (roman_string[i+1] == "D" or
                   roman_string[i+1] == "M")):
                number = number - 100
            elif (roman_string[i] == "X" and
                  roman_string[i+1] != "L" and
                  roman_string[i+1] != "C"):
                number = number + 10
            elif (roman_string[i] == "X" and
                  (roman_string[i+1] == "L" or
                   roman_string[i+1] == "C")):
                number = number - 10
            elif (roman_string[i] == "I" and
                  roman_string[i+1] != "V" and
                  roman_string[i+1] != "X"):
                number = number + 1
            elif (roman_string[i] == "I" and
                  (roman_string[i+1] == "V" or
                   roman_string[i+1] == "X")):
                number = number - 1
        else:
            if roman_string[i] == "C":
                number = number + 100
            elif roman_string[i] == "X":
                number = number + 10
            elif roman_string[i] == "I":
                number = number + 1
        if roman_string[i] == "M":
            number = number + 1000
        elif roman_string[i] == "D":
            number = number + 500
        elif roman_string[i] == "L":
            number = number + 50
        elif roman_string[i] == "V":
            number = number + 5
    return number
