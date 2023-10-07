n = int(input("n = "))
m = int(input("m = "))
    
if m > n:
     raise ValueError("n должен быть больше m")
    
a = []
sum_list = []

for i in range(n):
    a.append(int(input(f"a[{i}] = ")))

i = 0
while i < n - m + 1:
    sum_val = 0
    for j in range(i, i + m):
        sum_val += a[j]
    sum_list.append(sum_val)
    i += 1

for val in sum_list:
    print(val)



