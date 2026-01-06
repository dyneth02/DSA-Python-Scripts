def partition(array, lower_bound, upper_bound):
    pivot = array[lower_bound]
    start = lower_bound + 1
    end = upper_bound

    while True:
        while start <= end and array[start] <= pivot:
            start += 1
        while end >= start and array[end] >= pivot:
            end -= 1
        if start <= end:
            array[start], array[end] = array[end], array[start]
        else:
            break

    array[lower_bound], array[end] = array[end], array[lower_bound]
    return end

def quick_sort(array, lb, ub):
    if lb >= ub:
        return
    else:
        k = partition(array, lb, ub)
        quick_sort(array, lb, k - 1)
        quick_sort(array, k + 1, ub)

data = [10, 7, 8, 9, 1, 5]
print("Before Sorting:", data)
quick_sort(data, 0, len(data) - 1)
print("After Sorting:", data)
