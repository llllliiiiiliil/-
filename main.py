def sum1(n):
    a = 0
    for i in range(1,n+1):
        a += i * i
    return a

def sum2(n):
    a = 0
    a += n * (n + 1) * (2 * n + 1) // 6
    return a

print(sum2(1000000000000))
