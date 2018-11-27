import random

NUM_PER_LINES = 6
MIN = 1
MAX = 45

def main():
    num_picks = int(input("Enter number to quick picks to be generated"))
    while num_picks < 0:
        print("Please re-enter a valid value")
        num_picks = int(input("Enter number to quick picks to be generated"))
    for i in range(num_picks):
        quick_picks = []
        for j in range(NUM_PER_LINES):
            number = random.randint(MIN,MAX)
            while number in quick_picks:
                nummber = random.randint(MIN,MAX)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:4}".format(number) for number in quick_picks))

main()
