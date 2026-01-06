def multiply(M, n):
    if n == 1:
        return M
    else:
        return multiply(M, n - 1) + M

def __main__():
    while True:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num1 == -1 or num2 == -1:
            print("Output: Finished...")
            break
        elif num1 <= 0 or num2 <= 0:
            print("Invalid input. Please enter a positive integer.")
        else:
            print(f"Output: {multiply(num1, num2)}")


__main__()