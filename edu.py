numbers = set([1,2,3,4,5,6,7,8])#элемента множества не могут вызываться по индексу
letters = set("HELLO")
print(numbers)
print(letters)#вывод h e l o, соответственно они не повторяют переменные и каждая переменная в множестве является уникальной
numbers_and_letters = numbers | letters #объединения
numbers_with_letters = numbers & letters # пересечение
nimbers_minus_letters = numbers - letters #minus
numbbers_alta_letters = numbers ^ letters #симметричная разность
print(numbers_and_letters)
