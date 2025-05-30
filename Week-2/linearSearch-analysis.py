def linear_search(my_list, key):
    for i in range(len(my_list)):
        if my_list[i] == key:
            return i
    return -1

# Step 1 - Defining Variables

# Let n represent the size of the list my_list
# Let T(n) represent the number of operations performed by the the linear search function when it is passed with list of size n

# Step 2 - Counting the number of operations
def linear_search(my_list, key):
    for i in range(len(my_list)):   # 1 + 1 + n
        if my_list[i] == key:       # n
            return i                # 0
    return -1                       # 1

# Step 3 
# T(n) = 1 + 1 + n + n + 0 + 1

# Step 4
# T(n) = 3 + 2n

# Step 5
# Therefor, T(n) is O(n)
