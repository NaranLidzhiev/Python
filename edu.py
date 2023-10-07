def find_smallest(arr):
    smallest_el = arr[0]
    smallest_index = 0;
    for i in range(1, len(arr)):
        if (arr[i] < smallest_el):
            smallest_el = arr[i]
            smallest_index = i
    return smallest_index

arr = [13242,23,2,4,23,23,52,5]
print(find_smallest(arr))