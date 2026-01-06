def series_test(num):
    if num == 1:
        return 7
    else:
        return series_test(num - 1) + 4 * num + 1

while True:
    number = int(input("Enter a number: "))
    if number == -1:
        print("Output: Finished...")
        break
    elif number <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        print("Output: ", series_test(number))