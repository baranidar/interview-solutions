
#PMI - for recursion, we use principle of mathematical induction
def sumoofnnumbers(n):
    # 1) base case
    if n == 1:
        return 1
    
    # 2) Induction Hypothesis - assumption
    ans = sumoofnnumbers(n-1) 
    
    # 3) use base case and assumption to solve our problem
    return n + ans 
    

print(sumoofnnumbers(5))