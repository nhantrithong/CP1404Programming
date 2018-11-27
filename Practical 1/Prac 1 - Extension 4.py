def main():
    x = int(input("Please input your x value"))
    y = int(input("Please input your y value"))
    print("(1) - Show even numbers from x to y")
    print("(2) - Show odd numbers from x to y")
    print("(3) - Show the squares from x to y")
    print("(4) - Exit Program")
    choice = input("What you would like to do?")
    while choice not in ['1', '2', '3','4']:
        print("Please re-input a valid option")
        choice = input("What you would like to do? (1) - Show even numbers from x to y, (2) - Show odd numbers from x to y, (3) - Show the squares from x to y, (4) - Exit Program")
    while choice != "4":
        if choice == "1":
            for i in range(x,y+1):
                if(i%2 == 0):
                    print(i)
        if choice == "2":
            for i in range(x,y+1):
                if(i%2 != 0):
                    print(i)
        if choice == "3":
            for i in range(x,y+1):
                    print(i*i)
        choice = input("What you would like to do? (1) - Show even numbers from x to y, (2) - Show odd numbers from x to y, (3) - Show the squares from x to y, (4) - Exit Program")
    if choice == "4":
        print("Finished")

main()