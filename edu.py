class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None

    def push_back(self, val):
        p = Node(val)
        if self.is_empty():
            self.first = p
            self.last = p
            return
        self.last.next = p
        self.last = p

    def print_list(self):
        if self.is_empty():
            return
        p = self.first
        while p:
            print(p.val, end=" ")
            p = p.next
        print()

    def reverse_list(self):
        if self.is_empty() or self.first.next is None:
            return

        prev = None
        current = self.first
        next_node = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.first.next = prev

if __name__ == "__main__":
    l = LinkedList()
    for i in range(1, 6):
        l.push_back(str(i))

    l.print_list()
    l.reverse_list()
    l.print_list()
# Код, который я предоставил выше, является Python-версией исходного кода на C++. Давайте разберем его на части и объясним, что он делает:
# Node - это класс, представляющий узел (элемент) связанного списка. У каждого узла есть два атрибута:
# val: хранит значение, которое представляет данный узел (в данном случае, это строка).
# next: это указатель на следующий узел в списке. По умолчанию он устанавливается в None, что указывает на то, что это последний узел в списке.
# LinkedList - это класс, представляющий связанный список. У него есть следующие методы:
# __init__: Конструктор класса, который инициализирует пустой список, устанавливая атрибуты first и last в None.
# is_empty: Метод, который проверяет, пуст ли список, возвращая True, если first равен None.
# push_back: Метод для добавления нового элемента в конец списка. Он создает новый узел с указанным значением и обновляет last для указания на новый последний узел.
# print_list: Метод для вывода элементов списка на экран. Он перебирает все узлы, начиная с first, и выводит их значения через пробел.
# reverse_list: Метод для обращения списка. Этот метод переупорядочивает элементы списка в обратном порядке. Он использует три указателя (prev, current, next_node) для обхода списка и переназначения указателей next для каждого узла так, чтобы они указывали в обратном направлении.
# В блоке if __name__ == "__main__": создается экземпляр класса LinkedList, заполняется данными от 1 до 5 при помощи метода push_back, выводится исходный список с помощью print_list, а затем список обращается с использованием reverse_list и выводится снова, чтобы показать результат обращения.
# Таким образом, этот код реализует связанный список с методами для добавления элементов в конец списка, проверки на пустоту и обращения списка. Вы можете видеть, как эти методы используются в функции main, чтобы создать, заполнить и изменить связанный список, а затем вывести результаты на экран.