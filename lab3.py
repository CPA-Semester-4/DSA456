# Part - A

def factorial(number):
    rc = 1
    if(number > 0):
        rc = number * factorial(number - 1)
    return rc

print(factorial(5))

def linear_search(list, key, idx = 0, size = 0):
    if(size == 0):
        size = len(list) - 1

    if(idx > size):
        return -1
    else:
        if(list[idx] == key):
            return idx
        else:
            return linear_search(list, key, idx + 1, size)
        
print(linear_search([1, 2, 3, 4, 5], 3))

def binary_search(list, key, st = 0, end = None):
    if(end == None):
        end = len(list) - 1

    mid = (st + end)//2

    if(st > end):
        return -1
    else:
        if(list[mid] > key):
            return binary_search(list, key, st, mid-1)
        elif(list[mid] < key):
            return binary_search(list, key, mid + 1, end)
        else:
            return mid
        
print(binary_search([1, 2, 3, 4, 5], 1))

def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"{source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, helper)
    print(f"{source} to {destination}")
    tower_of_hanoi(n - 1, helper, source, destination)

num_disks = 3
tower_of_hanoi(num_disks, 1, 2, 3)

# Part B

# def function1(value, number):

    #  if (number == 0):                                    # 1

    #         return 1

    #  elif (number == 1):                                  # 1

    #         return value

    #  else:                                                

    #         return value * function1(value, number-1)     # 2 + T(n - 1)

# Let n be the number passed in function1
# Let T(n) be the number of operations performed by function1 when passed with number

# T(n) = 1 + 1 + 2 + T(n - 1)
# T(n) = 4 + T(n - 1)

# Working:
# T(n - 1) = 4 + T(n - 2)
# T(n - 2) = 4 + T(n - 3)
# .
# .
# .
# T(3) = 4 + 4 + 3 ---> There are n -1 4's
# T(2) = 4 + 3
# T(1) = 3
# T(0) = 2

# T(n) = 4 (n - 1) + 3 + 2
# T(n) = 4n + 1

# Therefore, T(n) is O(n)

# ---------------------------------------------------------


# def recursive_function2(mystring,a, b):
# 	if(a >= b ):							                #1
# 		return True
# 	else:
# 		if(mystring[a] != mystring[b]):				        #1
# 			return False
# 		else:							
# 			return recursive_function2(mystring,a+1,b-1)	#2 + S(n-1)

# def function2(mystring):
# 	return recursive_function2(mystring, 0,len(mystring)-1)	#2 + O(n)

# Step 1: Declaring Variables
# Let n be the size of the string.
# Let T(n) be the number of operations performed by function2 when passed with a string of length n.

# Let S(n) be the number of operations performed by recursive_function2 when passed with a string of length n.

# Step 2: Count the operations

# Step 3
# S(n) = 1 + 1 + 2 + S(n - 1)
# S(n - 1) = 4 + S(n - 2)
# S(n - 2) = 4 + S(n - 3)
# .
# .
# .
# S(4) = 4 + 4 + 4 + 2 (There are n-1 4's)
# S(3) = 4 + 4 + 2 (There are n 2's)
# S(2) = 4 + 2
# S(1) = 2

# Step 4
# S(n) = 4 (n-1) + 2 S(n) = 4n -2

# Step 5
# Therefore, S(n) = O(n) Also, T(n) = O(n)

# ---------------------------------------------------------

# function 3:
# for T(n) = T(n/2) + 3
# The big O performance would be O(log n) ---> calculaton done in function 4

# ---------------------------------------------------------

# def function3(value, number):
# 	if (number == 0):				        # 1
# 		return 1
# 	elif (number == 1):				        # 1
# 		return value
# 	else:
# 		half = number // 2			        # 2
# 		result = function3(value, half)		# T(n/2) = 1 + log n
# 		if (number % 2 == 0):			    # 2
# 			return result * result
# 		else:					
# 			return value * result * result	#2

# Step 1: Declaring Variables
# Let n be the number passed in function3
# Let T(n) be the number of operations performed by the function3 when passed with number n

# Step 2: Count number of operations

# Step 3
# T(n) = 1 + 1 + 2 + T(n/2) + 2 + 2

# Step 4
# T(n) = 8 + T(n/2)
# T(n/2) = 8 + T(n/4)
# T(n/4) = 8 + T(n/8)
# .
# .
# T(1) = 3
# T(0) = 2
# T(n) = 8 (1 + log n) + 2
# T(n) = 8 + 8 log n + 2
# T(n) = 10 + 8log n

# Therefore, T(n) is O(log n)