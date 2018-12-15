#done

from prac_06.guitarclass import Guitar

def main():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.4)
    print(guitar)
    print("This guitar with name: {}, is {} years old".format(guitar.name, guitar.get_age()))
    print("Vintage: {}".format(guitar.is_vintage()))


main()

