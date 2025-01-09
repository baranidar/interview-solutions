def factorial(n):
    if n == 1:
        return 1
    ans = 1
    for i in range(n,1,-1):
        ans *= i
    return ans


def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)
    
print(factorial(10))
print(factorial_recursive(10))

