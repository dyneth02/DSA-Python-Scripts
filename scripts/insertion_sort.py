def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

array = list(map(int, input("Enter a list of elements : ").split(" ")))
print("The unsorted array is : ", array)
insertion_sort(array)
print("The sorted array is : ", array)