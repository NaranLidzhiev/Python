def countdown(i):
    if i <= 0:
        print("end")
        return
    else:
        print(i)
        countdown(i-1)

countdown(12)