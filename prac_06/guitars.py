
from prac_06.guitarclass import Guitar

list = []

def main():
    print("My Guitars!")
    details()

def details():
    guitar_name = str(input("Name:"))
    if guitar_name in ['',' ','  ']:
        results()
    else:
        guitar_year = int(input("Year:"))
        guitar_cost = int(input("Cost:"))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        list.append(guitar)
        print(guitar,"added")
        print("")
        details()

def results():
    count = 0
    for i in list:
        count += 1
        final = ("Guitar {}: {}".format(count,i))
        print(final)



main()