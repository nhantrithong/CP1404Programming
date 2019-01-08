from prac_08.SilverServiceTaxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("The total fare is ${}".format(taxi.get_fare()))

main()