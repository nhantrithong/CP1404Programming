def main():
    cents = float(input("Please enter your cent value per kWh"))
    daily = float(input("Please enter your daily use in kWh"))
    days = float(input("Please enter your number of billing days"))
    total = (cents * daily * days)/100
    print("Your estimate electricity bill value totals to $" + str(total))

main()