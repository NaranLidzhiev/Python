

def tribonacci(signature, n):
    for i in range(0, n-len(signature)):
        signature.append(signature[-1] + signature[-2] + signature[-3])
    return signature[:n]
print(tribonacci([1,1,1], 10))