n = int(input())
print(n.bit_length() - (n & (n - 1) == 0))