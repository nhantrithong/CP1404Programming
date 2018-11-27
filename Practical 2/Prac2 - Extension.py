def main():
    try:
        character = input("Input a character: ")
        print("The ASCII code for",character,"is",ord(character))
    except TypeError:
        print("Invalid input")
    number = int(input("Please enter a number between {} and {}".format(33,127)))
    while number < 33 or number > 127:
        number = input("Please re-input a number between 33 and 127")
    else:
        print("The character for",number,"is",chr(number))


main()