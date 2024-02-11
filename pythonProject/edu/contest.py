def Kate_day(a,b, c, d):
    if d > b:
        return  a+ (d-b)*c
    else: return a


A,B,C,D = map(int,input().split())
print(Kate_day(A,B,C ,D))