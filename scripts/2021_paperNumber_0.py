def get_tri_num(num):
    if num == 1:
        return 1
    else:
        return get_tri_num(num-1) + num

while True:
    num = int(input("Enter a number: "))
    if num == -1:
        print("Output: Finished...")
        break
    elif num <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        print(f"Output: {get_tri_num(num)}")