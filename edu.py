def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = int((low+high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item: #если элемент посередине больше чем искомый, то верхней границей становится элемент, который стоит на позицию ниже срединного элемента
            high = mid -1
        else:
            low = mid +1  #если элемент посередине меньше чем искомый, то нижней границей становится элемент, который стоит на позицию выше срединного элемента
    return None
#то есть мы смотрим больше или меньше искомого значения наш элемент который у нас в guess и основываясь на этом двигаем границы, если больше то все цифры больше guess отбрасываются, если меньше, то все цифры выше guess отбрасываются
my_list = [1,2,4,6,7,8]
print(binary_search(my_list, 7))