def power(base, n):
    rc = 1                          # 1
    if(n > 0):                      # 1
        rc = power(base, n // 2)    # 2 + T(n/2)
        rc = rc * rc                # 2

        if(n % 2 == 1):             # 2
            rc *= base              # 1
    
    return rc                       # 1

# Let n be the value of the power to raise the base to
# Let T(n) be the num. of operations

# T(n) = 10 + T(n/2)
# T(n - 1) = 10 + T(n/4)
# T(2) = 10 + 10 + 3
# T(1) = 10 + 3
# T(0) = 3

# def power(base, n):
#     rc = 1
#     if n == 1:
#         return base
    
#     rc = base * power(base, n - 1)

#     return rc

print(power(2, 4))