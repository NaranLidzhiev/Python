def cake(n):
    k = 0
    while n > 1:
        n = n/2
        k += 1
    return k


N = int(input())
print(cake(N))

