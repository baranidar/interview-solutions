
#PMI - foor recursion, we use principle of mathematical induction
def power2(n):
    # 1) base case
    if n == 1:
        return 2
    
    # 2) Induction Hypothesis - assumption
    ans = power2(n-1) 
    
    # 3) use base case and assumption to solve our problem
    return 2*ans 
    

print(power2(5))