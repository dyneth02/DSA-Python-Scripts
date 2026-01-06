def bubble_sort(arr):
    if len(arr) == 0:
        return None
    else:
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

x = list(map(int, input("Enter a list of elements : ").split(" ")))
x = bubble_sort(x)
print("The array after sorting is : ", x)