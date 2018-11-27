TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

def main():
    tariff = float(input("Please select your tariff between either 11 or 31"))
    while tariff not in [11,31]:
        print("Please re-input valid option")
        tariff = float(input("Please select your tariff between either 11 or 31"))
    if tariff == 11:
        value = float(TARIFF_11)
    elif tariff == 31:
        tariff == float(TARIFF_31)
        value = float(TARIFF_31)
    daily = float(input("Please enter your daily use in kWh"))
    days = float(input("Please enter your number of billing days"))
    total = (value * daily * days)
    print("Your estimate electricity bill value totals to $" + str(total))

main()