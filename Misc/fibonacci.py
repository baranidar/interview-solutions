def fibonacci(n):
    lst = [0]
    a = 0
    b = 1
    lst.append(b)

    for i in range(n-2):
        c = a+b
        lst.append(c)
        a = b
        b = c

    print(lst)
    
def fibonacci_recursive(n, lst = []):
    if n == 0:
        return lst
 
    if len(lst) == 0:
        lst.append(0)
        lst.append(1)
        n -= 2

    lst.append(lst[-1]+lst[-2])
    return fibonacci_recursive(n-1, lst)



fibonacci(20)
output = fibonacci_recursive(20)
print(output)