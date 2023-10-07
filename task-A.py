sum = 0;

while True:
    a = input()
    print(a)
    if not a:
        break;
    if isinstance(a , int):
        print("good")
    else:
        print("bad")

