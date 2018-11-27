"Program to calculate and display a user's bonus based on sales."
"If sales are under $1000, the user gets a 10% bonus."
"If sales are $1000 or over, the bonus is 15%."

def main():
    sales = float(input("Enter sales: $"))
    if sales < 0:
        print("Please enter a valid sales value")
    if sales < 1000:
        value = sales + (sales * 0.1)
        print("Your bonus based on sales totals to a value of $" + str(value))
    elif sales >= 1000:
        value = sales + (sales * 0.15)
        print("Your bonus based on sales totals to a value of $" + str(value))
    main()

main()
