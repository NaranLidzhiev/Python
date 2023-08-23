import sys
# if (sys.argv != 2):
#     print("some shit happen")
#     raise SystemExit(1)
f = open("omega.txt")
lines = f.readlines()#читает все строки из файла  в список
f.close()

fvalues = [float(line) for line in lines] #каждый элемент lines превращаем в число с плавающей точкой

print("minimum: ", min(fvalues))
print("maximum: ", max(fvalues))