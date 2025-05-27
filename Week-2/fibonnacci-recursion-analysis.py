def fibonnacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        rc = 0
        i = 2
        while(i <= n):
            rc = a + b
            a = b
            b = rc
            i += 1
        return rc
    
print(fibonnacci(6))
    
def fibonnacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)
    
print(fibonnacci(6))
    
### Step - 1
# Let n represent the value we pass in the fibonnacci function
# Let T(n) reprsent the number of operations done by the function fibonacci given n as the argument

### Step - 2

def fibonnacci(n):                  # Number of Operations
    if n == 0:                      # 1
        return 0                    # 0
    elif n == 1:                    # 1
        return 1                    # 0
    else:                           
        a = 0                       # 1
        b = 1                       # 1
        rc = 0                      # 1
        i = 2                       # 1
        while(i <= n):              # n - 1
            rc = a + b              # 2 (n - 1)
            a = b                   # 2 (n - 1)
            b = rc                  # 2 (n - 1)
            i += 1                  # 2 (n - 1)
        return rc                   # 1

def fibonnacci(n):                                  # Number of operations
    if n == 0:                                      # 1
        return 0                                    # 0
    elif n == 1:                                    # 1
        return 1                                    # 0
    else:                                                         
        return fibonnacci(n-1) + fibonnacci(n-2)    # 3 + T(n-1) + T(n-2)

# T(n) = 5 + T(n-1) + T(n-2)

# T(0) = 2
# T(1) = 3
# T(2) = 3 + T(1) + T(0) = 5 + 3 + 3 + 2
# T(3) = 5 + T(2) + T(1) = 5 + 5 + 3 + 3 + 2 + 3
# T(4) = 5 + T(3) + T(2) = 5 + 5 + 3 + 3 + 2 + 3 + 3 + 3 + 2 [1 5, 5 3, 2 2]
# T(5) = 5 + T(4) + T(3) = 5 + 5 + 3 + 3 + 2 + 3 + 3 + 3 + 2 + 5 + 3 + 3 + 2 + 3 [3 5, 8 3, 3 2]
# T(6) = 5 + T(5) + T(4) = 5 + 5 + 5 + 3 + 3 + 2 + 3 + 3 + 3 + 2 + 5 + 3 + 3 + 2 + 3 + 5 + 3 + 3 + 2 + 3 + 3 + 3 + 2 [5 5, 13 3, 5 2]
# T(n) =  
    
