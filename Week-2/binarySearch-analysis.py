def binary_search(my_list, key):
    rc = -1
    low = 0
    high = len(my_list) - 1

    while low <= high and rc == -1:
        mid = (low + high) // 2

        if my_list[mid] > key:
            high = mid - 1
        elif my_list[mid] < key:
            low = mid + 1
        else:
            rc = mid
    
    return rc

# Step 1 
# Let n be the size of the my_list 
# Let T(n) be the number of operations performed by the binary_search function when it is passed with a list of size n

# Step 2
def binary_search(my_list, key):
    rc = -1                             # 1
    low = 0                             # 1
    high = len(my_list) - 1             # 1 + 1 + 1 

    while low <= high and rc == -1:     # 3 * (1 + log n)
        mid = (low + high) // 2         # 3 * (1 + log n)

        if my_list[mid] > key:          # (1 + log n)
            high = mid - 1              
        elif my_list[mid] < key:        # (1 + log n)
            low = mid + 1               # 2 * (1 + log n)
        else:                           
            rc = mid
    
    return rc                           # 1

# Step 3:
# T(n) = 1 + 1 + 1 + 1 + 1 + 3 * (1 + log n) + 3 * (1 + log n) + (1 + log n) + (1 + log n) + 2 * (1 + log n) + 1

# Step 4:
# T(n) = 6 + 10 (1 + log n)
# T(n) = 16 + 10(log n)

# Step 5:
# Therefore T(n) = O(log n)