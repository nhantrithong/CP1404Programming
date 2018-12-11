#Write a program that ask for user age and prints whether its odd or even
# - should not crash if enter an even number
# - should not allow invalid input
# - while loop to make sure valid number will be eventually selected

def main():
    try:
        age = int(input("Enter age: "))
        while age < 0 or age > 110:
            print("Please enter a valid age value")
            age = int(input("Enter age: "))
        if age % 2 == 0:
            print("This is an even number")
        elif age % 2 != 0:
            print("This is an uneven/odd number")
    except ValueError:
        print("Error")
main()