def factorial(n):                   
    if n <= 1:                      
        return 1                    
    
    return n * factorial(n - 1)     

print(factorial(5))

### Analysis of recursive factorial

# Step 1 - Declare your variables
# 1 - Let n respresent the value being passed to the f(n) factorial
# 2 - T(n), number of operations done by the f(n) factorial given the value n

def factorial(n):                   # Number of Operations
    if n <= 1:                      # 1
        return 1                    # 1
    
    return n * factorial(n - 1)     # 3 + T(n - 1) 
                                        # T(n), number of operations done by the f(n) factorial given the value n
                                        # Here we are calling factorial() with n - 1 so, the number of operations done by that is T(n - 1)

# T(n) = 1 + 1 + 3 + T(n - 1)
# T(n) = 5 + T(n - 1)

# T(n-1) = 5 + T(n - 2)
# T(n-2) = 5 + T(n - 3)
# T(n-3) = 5 + T(n - 4)

# T(1)   = 2
# T(2)   = 5 + 2
# T(3)   = 5 + 5 + 2
# T(4)   = 5 + 5 + 5 + 2
# .
# .
# .
# T(n)   = 5 + 5 + 5 + ..... + 2 <---- There are n - 1 5's here
#        = 5(n - 1) + 2
#        = 5n - 3  for all n > 1

# Therefore T(n) is O(n)
