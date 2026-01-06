def power(base, exp):
    if exp == 0 or base == 1:
        return 1

    return base * power(base, exp - 1)


while True:
    x = int(input("Enter number for x: "))
    n = int(input("Enter number for n: "))
    if x == -1 or n == -1:
        break

    print(power(x, n))
