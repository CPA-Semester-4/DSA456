
### NOTES:

# 1. Determine if the function has a prototype that supports recursion
#   * the arguments given to this function needs to support recursion.. can I give it something that leads it towards a simpler solution
# 2. What value(s) can we provide that will lead to a base case


# Write the following function iteratively and recursively and analyze both

# Function return base^n
# Challenge: Write power() recursively so that its run time is better than O(n)

# def power(base, n):
#     rc = 1
#     for i in range(n):
#         rc *= base
#     return base

### Trying to find the recursion logic

# 5, 5 = 5 * 5 * 5 * 5 * 5
# 5, 6 = 5 * (power(base, n-1))
# n = 1 return base

def power(base, n):                         
    if n == 1:
        return base
    
    return base * (power(base, n - 1))

## Analysis of of power(base, n) 
def power(base, n):                         
    rc = 1                                    # 1
    if n > 0:                                 # 1
        rc = base * (power(base, n - 1))      # 3 (=, *, -) + T(n - 1)
                                                                     # T(n - 1) coemes from the power() call, we call power with n - 1 as second arguemnt.
    return rc                                 # 1

# let n represents the value for the exponent in this function
# let T(n) represent the number of operations done by power function when n is passed as the 2nd argument.

# T(n) = 1 + 1 + 3 + T(n - 1) + 1
# T(n) = 6 + T(n - 1)

# T(n-1) = 6 + T(n - 2)
# T(n-2) = 6 + T(n - 3)
# T(n-3) = 6 + T(n - 4)
# .
# .
# .
# T(2) = 6 + T(1)
# T(1) = 6 + T(0)
# T(0) = 3

# T(2) = 6 + 6 + 3
# T(3) = 6 + 6 + 6 + 3
# T(n) = 3(n) + 3

def power(base, n):
    rc = 1                      # 1
    if (n > 0):                 # 1
        tmp = power(base, n//2) # if we call the function twice here, the run time will go from log to O(n) - power(base, n//2) * power(base, n//2)                   2 + T(n/2)
        rc  = tmp * tmp         # 2
        if(n % 2 == 1):         # 2
            rc = rc*base        # 2

    return rc                   # 1

print(power(2, 3))

### Analysis
# T(n) = 1 + 1 + 2 + T(n/2) + 2 + 2 + 2 + 1
# T(n) = 11 + T(n/2)
# ...
# ...
# T(1) = 11 + T(0)
# T(0) = 3

# Thinking through the numbers we keep taking n and dividing by 2. our calls are made with n, n/2, n/4, n/8 ... 1 = n / n
# argument value | alternate expression
# n              | n/1 = n/2^0
# n/2            | n/2^1 
# n/4            | n/2^2
# n/n            | 1 = n/2^k = n/2^(logn)

# Therefore, it took 1 + (logn) divisions to go from n to 1
# Therefore, T(n) = 11 (1 + log n) + 3
                #   = 11 + 11 log n + 3
                #   = 14 + 11 log n
                # T(n) is O(log n)

