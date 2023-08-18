A, B, C, D = map(int, input().split())
total_cost = A
if (D> B):
    total_cost += C*(D-B)

print(total_cost)