def quick_sort(array):
    if len(array)<2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) +[pivot] +quick_sort(greater)
print(quick_sort([1,1,3,3,2,34,24,43,2,4,234,23,43,4,5,5,43,5,25,2]))