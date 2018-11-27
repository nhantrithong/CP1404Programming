def main():
    name = str(input("Please input your name"))
    option = str(input("Please selected an option: (H) - Hello, (G) - Goodbye, (Q) - Quit")).upper()
    while option not in ['H','G','Q']:
        print("Please re-input a valid option")
        option = str(input("Please selected an option: (H) - Hello, (G) - Goodbye, (Q) - Quit")).upper()
    while option != "Q":
        if option == "H":
            print("Hello", name)
        elif option == "G":
            print("Goodbye", name)
        else:
            print("Invalid Message")
        option = str(input("Please selected an option: (H) - Hello, (G) - Goodbye, (Q) - Quit")).upper()
    if option == "Q":
        print("Finished")

main()



