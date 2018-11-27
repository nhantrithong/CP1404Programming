numbers = []
def main():
    from statistics import mean
    for i in range(1,6):
        number = int(input("Enter number " + str(i)))
        numbers.append(number)
    print("The first number is ",str(numbers[0]))
    print("The last number is ",str(numbers[4]))
    print("The smallest number is ",str(min(numbers)))
    print("The largest number is ",str(max(numbers)))
    avg = sum(numbers) / 5
    print("The average of the numbers is",avg)

main()