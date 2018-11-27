totalprice=[]
def main():
    item = int(input("Please enter the number of items: "))
    while item < 0:
        print("Invalid value, please re-input a postive number of items")
        item = int(input("Please enter the number of items"))
    print("*"*20)
    for i in range(0,item):
        price = float(input("Please enter the price of the item: $"))
        totalprice.append(price)
    print("*"*20)
    for b in totalprice:
        print("Price of item: $" + str(b))
    finalprice = sum(totalprice)
    print("=> The grand total of your purchase is equal to $" + str(finalprice))
    if finalprice >=100:
        print("=> The total price with discount bonus applied is $" + str(finalprice - (finalprice * 0.1)))


main()