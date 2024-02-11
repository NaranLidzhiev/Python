def Kate_shift(num, time, floors, cow):
    if n <= 2 or time >= 100:
        return 0
    maximus = max(floors)
    minimus = min(floors)
    if cow > t or maximus - minimus <= time:
        return min(maximus - minimus + maximus - cow, maximus -minimus + cow - minimus)
    else:
        return maximus - minimus


n, t = map(int, input().split())
floors = list(map(int, input().split()))
cow = int(input())
print(Kate_shift(n, t, floors, cow))