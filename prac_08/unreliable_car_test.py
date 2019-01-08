from prac_08.unreliable_car import UnreliableCar

def main():
    car1 = UnreliableCar("UR.Car",100,90)
    print(car1)
    print("The current distance driven is {}".format(car1.drive(80)))
    print(car1)
    print("The current distance driven is {}".format(car1.drive(10)))
    print(car1)

main()