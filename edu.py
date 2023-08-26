try:
    f = open("file.txt")
except IOError as e:
    print(e)