import re
from sys import stdin
from collections import deque
import sys
#первая строка это идентификаторы уязвимых библиотет
#вторая строка это идентификаторы прямых зависимостей проекта, разделенных пробелом
#каждая последующая строка содержит идентификатор зависимости и идентификаторы библиотек, от которых она зависит, разделенных пробелом.
#суть в том что мы должны отследить путь от идентификатора прямой зависимости до уязвимой библиотеки.
#если мы сразу не нашли путь до уязвимой библиотеки, то мы должны сопоставить идентификаторы билбиотек для нашего идентификатора зависимости 
# и посмотреть будут ли эти библиотеки в дальнейшем идентификаторами зависимости, если да, то повторяем поиск до того момента пока не найдем юязвимую юиюлиотеку
#надо реализовать такую вещь, чтобы библиотека в ключе совпадала с vulnerable libraies, если она не совпадает, 
# то смотрим какиеи библиотеки в ключе совпадает по названию с другими ключами, если совпадение есть, то перебираем этот ключ и так пока не найдем уязвимую библиотеку. 
# Параллельно с этим мы должны записывать в строку ключи с которыми мы работаем и, если мы находим библиотеку, то мы добавляем библиотеку в конец строки, выводим строку и завершаем операцию.
# sys.setrecursionlimit(2000)
def find(slov, string, el):
    string += el + " "
    for i in range(len(slov)):
        if slov[i] in direct:
                # string += slov[i]+" "
              find(dep[slov[i]], string, slov[i])
        if slov[i] in vulnerable_libraries:
            # print("slov",i," = ", slov[i], " in vulnerable_libraries")
            temp = string
            string += slov[i]+" "
            if string not in array:
                # print("string = ", string, " is APPENDED")
                array.append(string)
                string = temp
# главная проблема в том, что когда он видит зависимость и посылается к ней, а библиотека ссылается не него же, то выходит ошибка
#            #осталость сделать так чтобы зависимости выводились полностью, а также не повторялись
vulnerable_libraries = input().split()
direct_dependencies = input().split()
var = ""
 #Нужно сдклать так, чтобы наш цикл не останавливался при наличии слова в vulnerable libraries, а просто так, потому что vulnerable libraires могут быть в directs
# print(vulnerable_libraries)
# print(direct_dependencies)
dep = {} #тут у нас словарь(зависимость: библиотеки)
direct = deque([])#тут лежат идентификаторы которые мы получили
var = deque([]) #
arr = deque([])
array = deque([])

for line in stdin:
    arr = line.split()
    dep[arr[0]] = arr[1:]
    direct.append(arr[0])
# print(direct)
# # print(dep)
for i in range(len(direct_dependencies)):
    if direct_dependencies[i] in vulnerable_libraries and direct_dependencies[i] != var:
        print(direct_dependencies[i])
        var = direct_dependencies[i]
StR = ""
for i in range(0, len(direct)):
    if direct[i] in direct_dependencies:
        # print("direct [",i, "] = ", direct[i], " in direct dependencies")
        # StR = direct[i] + " "
        item = direct[i]
        find(dep[direct[i]], StR, item)

for i in range(len(array)):
    print(array[i])

# for i in range(0, len(direct)):
#     find(direct[i], dep[direct[i]], direct)
#     v = dep[direct[i]]
#     for j in range(0, len(v)):
#         if v[j] in vulnerable_libraries:
#             print(direct[i], " ",v[j] )
#         else:
#             if v[j] in direct:
#                 pass
# unity = []
# for i in range(0, len(var)):
#     for j in range(0, len(vulnerable_libraries)):
#         if var[i] == vulnerable_libraries[j]:
#             unity.append(var[i])

# print(unity)



