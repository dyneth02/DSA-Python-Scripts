def how_many_permutations(arr):
    if len(arr) == 0 or len(arr) == 1:
        return 1
    else:
        return len(arr) * how_many_permutations(arr[:-1])

def show_permutations(string, pocket = ""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[:i]
            back = string[i+1:]
            together = front + back
            show_permutations(together, pocket + letter)

x = list(input("Enter a list of elements : ").split(" "))
print("The number of permutations are : ", how_many_permutations(x))
show_permutations("ABC")
