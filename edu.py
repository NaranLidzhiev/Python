def find_min(array):
    min_el = array[0]
    min_index = 0
    for i in range(1, len(array)):
        if array[0] < min_el:
            min_el = array[0]
            min_index = i
    return min_index

def sort(array):
    new_array = []
    for i in range(len(array)):
        smallest = find_min(array) #находим индекс минимального элемента
        new_array.append(array.pop(smallest))
        print(array) #одновременно забиваем в новыый массив минимальный элемент и одновременно удаляем его из первичного массива
    return new_array

sort([1,2,23,2,4,4,2,4,7,132,3,1])