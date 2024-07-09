def tribonacci(n):
    F = [num for num in range(38)]
    F[0] = 0
    F[1] = F[2] = 1
    for i in range(3, n + 1):
        F[i] = F[i - 1] + F[i - 2] + F[i - 3]
        
    return F[n]

print(tribonacci(0)) # 0
print(tribonacci(1)) # 1
print(tribonacci(2)) # 1
print(tribonacci(3)) # 2
print(tribonacci(4)) # 4
print(tribonacci(5)) # 7
print(tribonacci(25)) 
