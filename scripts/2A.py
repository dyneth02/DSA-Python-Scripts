def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def get_median(arr):
    med_position = (len(arr) + 1) / 2
    if not len(arr) % 2 == 0:
        return arr[int(med_position - 1)]
    else:
        lower = arr[int(med_position - 1)]
        upper = arr[int(med_position)]
        return (lower + upper) / 2

def get_range(arr):
    return arr[-1] -  arr[0]


array = list(map(int, input("Enter a list of elements : ").split(" ")))
print("The unsorted array is : ", array)
insertion_sort(array)
print("The sorted array is : ", array)

print("The median is : ", get_median(array))
print("The range is : ", get_range(array))

